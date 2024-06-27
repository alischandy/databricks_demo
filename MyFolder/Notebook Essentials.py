# Databricks notebook source
print('hello world')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 'Hello world from SQL'

# COMMAND ----------

# MAGIC %md
# MAGIC ### Hello world

# COMMAND ----------

# MAGIC %run /Workspace/Includes/Setup

# COMMAND ----------

print(name) # name is defined in the Setup file

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

display(files)

# COMMAND ----------


