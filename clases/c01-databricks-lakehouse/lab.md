# Lab 1 — Primer activo gobernado en el Lakehouse

**Duración:** 70 min · **Modalidad:** individual dentro del equipo (cada persona deja su propia tabla; el equipo hace un solo PR)

## Objetivo

Dejar los datos de demanda y pérdidas como una tabla Delta en Unity Catalog, creada desde código que vive en el repositorio, con metadatos de ingesta y con historial de versiones.

## Antes de empezar

| Requisito | Cómo verificarlo |
|---|---|
| Invitación al workspace del curso aceptada | Puedes entrar y en **Catalog** ves el catálogo `workspace` |
| Cuenta de GitHub | Puedes abrir github.com con tu usuario |
| Fork de `Databricks-to-XM` | Existe `github.com/<tu-usuario>/Databricks-to-XM` |
| GitHub vinculado a Databricks | **Settings → Linked accounts → GitHub**, con un token con permiso `repo` |

## Pasos

### 1. Entrar al workspace
Inicia sesión en el workspace compartido. Ve a **Catalog** y confirma que ves el catálogo `workspace`. Ese es el catálogo por defecto de Free Edition; en la clase 3 creamos `dev`, `qa` y `prod`.

### 2. Fork y Git folder
1. En GitHub, **Fork** de `Databricks-to-XM` a tu cuenta.
2. En Databricks: **Workspace → tu carpeta de usuario → Create → Git folder**. URL: la de tu fork. Proveedor: GitHub.
3. Abre el Git folder y crea la rama `feature/<equipo>-c01-primera-tabla` (botón de rama arriba a la izquierda → **Create branch**).

### 3. Esquema y volumen
En un notebook nuevo (o en el editor SQL) ejecuta, reemplazando `<usuario>` por tu nombre corto sin puntos ni tildes:

```sql
CREATE SCHEMA IF NOT EXISTS workspace.c01_<usuario>;
CREATE VOLUME IF NOT EXISTS workspace.c01_<usuario>.raw;
```

Luego, en **Catalog → workspace → c01_<usuario> → raw → Upload to this volume**, sube `data/raw/DemandaPerdidas.xlsx` (está en tu fork; descárgalo de GitHub si no lo tienes local).

### 4. Abrir el notebook del lab
Dentro del Git folder: `clases/c01-databricks-lakehouse/notebooks/lab01_primera_tabla_delta`. En el widget `usuario` escribe el mismo valor del paso 3. No hay clúster que crear: el notebook se ejecuta en serverless.

### 5. Crear la tabla Delta
Ejecuta las celdas de la sección **Bronze**. Lee el Excel con pandas, lo convierte a Spark, agrega `_ingested_at` y `_source_file` y escribe `workspace.c01_<usuario>.demanda_raw`.

### 6. Consultar
Ejecuta las celdas de **Verificación**. Debes obtener:

| Métrica | Valor esperado |
|---|---|
| Filas | 145.408 |
| Filas por `CodigoVariable` | 72.704 y 72.704 |
| Series activas (agente × mercado × tipo × CIIU) | 355 |
| Rango de `Fecha` | 2026-01-01 a 2026-07-25 |

### 7. Historial y time travel
Vuelve a ejecutar la celda de escritura. Luego:

```sql
DESCRIBE HISTORY workspace.c01_<usuario>.demanda_raw;
SELECT count(*) FROM workspace.c01_<usuario>.demanda_raw VERSION AS OF 0;
```

Deben aparecer al menos dos versiones.

### 8. Commit y push
En el Git folder: botón de Git → revisa los cambios → mensaje `feat(c01): primera tabla Delta de demanda` → **Commit & Push**. Verifica el commit en tu fork en GitHub. Un integrante del equipo abre el PR hacia `main` de su fork; otro equipo lo revisa (comentario mínimo: "¿el notebook tiene algo hard-codeado?").

## Criterios de aceptación

- [ ] `workspace.c01_<usuario>.demanda_raw` existe, tiene 145.408 filas e incluye `_ingested_at` y `_source_file`
- [ ] `DESCRIBE HISTORY` muestra al menos 2 versiones
- [ ] El commit es visible en tu fork y el PR del equipo está abierto

## Extensión opcional

¿Cuántas series tienen datos los 206 días? ¿Cuáles no y cuántos días les faltan? Escribe la consulta en la última celda del notebook. La usaremos en la clase 2 para diseñar Silver.

## Problemas frecuentes

| Síntoma | Causa probable |
|---|---|
| `TABLE_OR_VIEW_NOT_FOUND` | El widget `usuario` no coincide con el esquema del paso 3 |
| `No such file` al leer el Excel | El archivo quedó en la carpeta del workspace, no en el volumen |
| Push rechazado | GitHub no está vinculado en **Linked accounts** o el token no tiene permiso `repo` |
| `ModuleNotFoundError: openpyxl` | Ejecuta la celda `%pip install openpyxl` que está al inicio del notebook |

## Así sería en Azure Databricks

| Hoy | En XM |
|---|---|
| Catálogo `workspace` | Catálogo `dev` en el workspace de desarrollo, con storage en ADLS Gen2 |
| Subir el Excel a mano al volumen | El archivo llega a un contenedor de ADLS (external location) y Auto Loader lo ingiere (clase 4) |
| Identidad por correo | Microsoft Entra ID; grupos sincronizados con SCIM |
| Git folder con token personal | Git folder con service principal o Azure Repos; despliegue por bundle (clase 13) |
