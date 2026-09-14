# Datos del caso

`DemandaPerdidas.xlsx` — demanda real y pérdidas de energía por operador de red, mercado de comercialización, tipo de mercado y actividad económica (CIIU).

| Columna | Descripción |
|---|---|
| FechaPublicacion | Fecha en que se publicó el registro (una misma `Fecha` puede publicarse varias veces) |
| Fecha | Día al que corresponde el valor |
| CodigoSICAgente | Código del operador de red |
| TipoMercado | Regulado / No Regulado |
| MercadoComercializacion | Mercado de comercialización |
| ClasificacionIndustrial | Sección CIIU (solo en No Regulado; `SIN CLASIFICAR` en Regulado) |
| Valor | kWh |
| CodigoVariable | `DdaReal` o `PerdidasEnergia` |

Formato largo. ~145 mil filas, 355 series activas, 2026-01-01 a 2026-07-25.

Uso exclusivo del curso.
