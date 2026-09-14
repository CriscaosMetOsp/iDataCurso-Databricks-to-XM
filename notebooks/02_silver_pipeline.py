# Databricks notebook source
# MAGIC %md
# MAGIC # Lakeflow Declarative Pipeline Bronze -> Silver con expectations
# MAGIC Clase 5. Notebook delgado: recibe parámetros del job y llama a `xm_demanda`.

# COMMAND ----------

dbutils.widgets.text("catalog", "dev")
catalog = dbutils.widgets.get("catalog")

# COMMAND ----------

# Se completa en Clase 5.
