# Rúbrica por hito

| Nivel | Descripción |
|---|---|
| 1 Inicial | El artefacto existe pero no cumple los criterios de aceptación del lab |
| 2 Funcional | Cumple los criterios; sin tests ni documentación |
| 3 Sólido | Cumple criterios, con tests, configuración externa y PR revisado |
| 4 Operable | Además, documentado (ADR/README), desplegable por bundle y con monitoreo o alerta |

| Hito | Clase de cierre | Evidencia |
|---|---|---|
| H1 Pregunta analítica | 2 | `docs/architecture.md`, ADR-001 |
| H2 Arquitectura y fuentes | 4 | Bronze idempotente con historial de publicaciones |
| H3 Gobierno, permisos y calidad | 6 | Catálogos y grants; pipeline con expectations; Silver |
| H4 Pipeline y Gold | 8 | Tabla de features; paquete con tests en CI |
| H5 Modelo, experimento y despliegue | 11 | Modelo registrado; inferencia batch; endpoint; app |
| H6 Operación, CI/CD y consumo | 15 | Job programado; bundle en 3 targets; CI/CD; monitor; runbook |
