# Databricks notebook source
# MAGIC %md
# MAGIC # Entrenamiento reproducible y registro del modelo en Unity Catalog
# MAGIC Clase 10. Notebook delgado: recibe parámetros del job y llama a `xm_demanda`.

# COMMAND ----------

dbutils.widgets.text("catalog", "dev")
catalog = dbutils.widgets.get("catalog")

# COMMAND ----------

# Se completa en Clase 10.
