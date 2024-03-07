from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()

df = spark.read.table("samples.nyctaxi.trips1")
df.show(5)
