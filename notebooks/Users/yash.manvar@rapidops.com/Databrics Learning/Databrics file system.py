# Databricks notebook source
import mlflow

# COMMAND ----------

mlflow.log_param("my", "param")
mlflow.log_metric("score", 100)
mlflow.end_run()


# COMMAND ----------

