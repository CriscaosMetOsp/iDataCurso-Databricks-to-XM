# Arquitectura de la solución

Se completa en la clase 2.

## Capas

| Capa | Esquema | Tabla | Granularidad | Dueño | Frescura |
|---|---|---|---|---|---|
| Bronze | `bronze_energia` | `demanda_raw` | fila publicada | | |
| Silver | `silver_energia` | `demanda_diaria` | serie-día | | |
| Silver | `silver_energia` | `dim_ciiu` | sección CIIU | | |
| Gold | `gold_energia` | `features_demanda_diaria` | serie-día | | |
| Gold | `gold_energia` | `pronostico_demanda` | serie-día-horizonte | | |

## Diagrama

(Free Edition vs. Azure Databricks)
