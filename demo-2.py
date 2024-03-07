from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.getOrCreate()

df = spark.read.table("samples.nyctaxi.trips1")
df.show(5)


# spark.read.table("samples.nyctaxi.trips").show(5)