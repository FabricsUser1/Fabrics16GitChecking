# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "bd5ba448-9952-4e8e-adf2-029339b49d93",
# META       "default_lakehouse_name": "TestLH",
# META       "default_lakehouse_workspace_id": "9a4fe962-8e3c-4f62-83df-502596959994",
# META       "known_lakehouses": [
# META         {
# META           "id": "bd5ba448-9952-4e8e-adf2-029339b49d93"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "default_warehouse": "aa03119b-7cb7-45c5-82af-8e839c48531c",
# META       "known_warehouses": [
# META         {
# META           "id": "aa03119b-7cb7-45c5-82af-8e839c48531c",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

source_path = "Files/sample_datasets/city_safety_seattle.csv"

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(source_path)
)

display(df.limit(10))
df.printSchema()

print("Total rows:", df.count())# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
