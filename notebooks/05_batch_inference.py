# Databricks notebook source
# MAGIC %md
# MAGIC # Inferencia batch a gold_energia.pronostico_demanda
# MAGIC Clase 11. Notebook delgado: recibe parámetros del job y llama a `xm_demanda`.

# COMMAND ----------

dbutils.widgets.text("catalog", "dev")
catalog = dbutils.widgets.get("catalog")

# COMMAND ----------

# Se completa en Clase 11.
