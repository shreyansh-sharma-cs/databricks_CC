
# src_conn is the MongoDB connection string.
# db_name is the MongoDB database name.

src_conn = dbutils.secrets.get(scope="mongodb", key="src_conn")
db_name = dbutils.secrets.get(scope="mongodb", key="database")

# collection_name contains the MongoDB collection to be read.

collection_name = "customers"

# Read customer data from MongoDB into a Spark DataFrame.
#  schema:
# ID (integer)
# Customer_Name (string)
# City (string)
# Age (integer)

customer_df = (
    spark.read
         .format("mongodb")
         .option("spark.mongodb.read.connection.uri", src_conn)
         .option("database", db_name)
         .option("collection", collection_name)
         .load()
)

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, desc

# Create a window partitioned by city and ordered by age desc
# The customer with row number 1 will be the oldest customer in each city.

city_window = Window.partitionBy("City").orderBy(desc("Age"))

oldest_customer_df = (
    customer_df
    .withColumn("row_num", row_number().over(city_window))
    .filter("row_num = 1")
    .drop("row_num")
)

# Write the oldest customer from each city to a Delta table.

oldest_customer_df.write \
                  .format("delta") \
                  .mode("overwrite") \
                  .save("/mnt/delta/sample_data")
