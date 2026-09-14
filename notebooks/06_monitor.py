# Databricks notebook source
# MAGIC %md
# MAGIC # Monitoreo de datos y de desempeño del modelo
# MAGIC Clase 15. Notebook delgado: recibe parámetros del job y llama a `xm_demanda`.

# COMMAND ----------

dbutils.widgets.text("catalog", "dev")
catalog = dbutils.widgets.get("catalog")

# COMMAND ----------

# Se completa en Clase 15.
