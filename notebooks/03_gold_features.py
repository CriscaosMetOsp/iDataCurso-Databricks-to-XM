# Databricks notebook source
# MAGIC %md
# MAGIC # Construcción de features en Gold
# MAGIC Clase 7. Notebook delgado: recibe parámetros del job y llama a `xm_demanda`.

# COMMAND ----------

dbutils.widgets.text("catalog", "dev")
catalog = dbutils.widgets.get("catalog")

# COMMAND ----------

# Se completa en Clase 7.
