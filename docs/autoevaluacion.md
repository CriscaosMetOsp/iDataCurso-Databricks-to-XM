# Autoevaluación por hito

No hay calificación. Cada laboratorio incluye una celda `verificar()` que comprueba los criterios de aceptación. Esta lista es el resumen por hito para saber dónde estás.

Cómo compararte con la solución de referencia al cierre de cada clase:

```bash
git remote add upstream https://github.com/<docente>/Databricks-to-XM.git   # una sola vez
git fetch upstream --tags
git diff s01 -- clases/c01-databricks-lakehouse notebooks src   # cambia s01 por el tag de la clase
```

| Hito | Clase de cierre | Sé que terminé cuando… |
|---|---|---|
| H1 Pregunta analítica | 2 | `verificar()` del lab 1 en verde; `docs/architecture.md` con las tablas por capa y ADR-001 escrita |
| H2 Arquitectura y fuentes | 4 | Bronze idempotente: cargar dos veces el mismo archivo no duplica; el historial conserva las publicaciones |
| H3 Gobierno, permisos y calidad | 6 | Catálogos `dev/qa/prod` con grants; pipeline con expectations y tabla de cuarentena; Silver en formato ancho |
| H4 Pipeline y Gold | 8 | Tabla de features documentada; `pytest tests/unit` y `ruff check .` en verde en CI del fork |
| H5 Modelo, experimento y despliegue | 11 | Modelo registrado en UC con firma y alias `champion`; `pronostico_demanda` poblada por job; endpoint y app responden |
| H6 Operación, CI/CD y consumo | 15 | Bundle desplegado en `dev` y `qa`; CI/CD dispara por PR y por tag; monitor de drift con alerta; runbook escrito |

Niveles orientativos para cada hito, por si quieres ir más allá:

| Nivel | Qué significa |
|---|---|
| Funcional | `verificar()` en verde |
| Sólido | Además: tests para toda función de `src/`, configuración en `conf/`, nada hard-codeado |
| Operable | Además: desplegable por bundle, documentado (ADR/README) y con alerta o monitor |
