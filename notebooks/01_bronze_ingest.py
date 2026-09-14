# Databricks notebook source
# MAGIC %md
# MAGIC # Ingesta Bronze con Auto Loader desde el volumen raw
# MAGIC Clase 4. Notebook delgado: recibe parámetros del job y llama a `xm_demanda`.

# COMMAND ----------

dbutils.widgets.text("catalog", "dev")
catalog = dbutils.widgets.get("catalog")

# COMMAND ----------

# Se completa en Clase 4.
