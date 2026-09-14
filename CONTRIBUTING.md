# Convenciones del repositorio

| Tema | Regla |
|---|---|
| Ramas | `main` protegida. Trabajo en `feature/<equipo>-c<clase>-<tema>`. PR obligatorio con un revisor de otro equipo |
| Commits | Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:` |
| Nombres en Unity Catalog | `<ambiente>.<capa>_<dominio>.<entidad>` → `dev.silver_energia.demanda_diaria`. snake_case, sin tildes |
| Jobs y pipelines | `[xm-demanda] <verbo>_<objeto>` (el ambiente lo agrega el bundle) |
| Tags en UC | `dominio=energia`, `capa=<bronze|silver|gold>`, `owner=<equipo>` |
| Configuración | Nada hard-codeado. Catálogo, rutas y parámetros salen de `conf/<env>.yml` y variables del bundle |
| Secretos | Solo en secret scopes. Nunca en el repo |
| Notebooks | Delgados: orquestan, no implementan. La lógica vive en `src/xm_demanda/` |
| Modelos | Registrados en UC como `<env>.models.demanda_7d`, con firma y ejemplo de entrada; alias `champion` / `challenger` |
| Tests | `tests/unit` para toda función de `src/`; `tests/integration` corre en `dev` vía bundle |
| Decisiones | Una ADR por decisión de arquitectura en `docs/adr/` |

## Flujo de trabajo por clase

1. Crear rama desde `main`.
2. Completar el laboratorio (`clases/cXX/lab.md`) hasta cumplir los criterios de aceptación.
3. `ruff check . && pytest tests/unit` en local.
4. Abrir PR. Revisión cruzada. Merge.

## Entorno local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
databricks auth login --host <workspace-url>
```
