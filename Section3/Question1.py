# src_conn is the MongoDB connection string used to connect to the source database.
# db_name contains the name of the MongoDB database
# collection_name is the MongoDB collection that will be read
# mongo_df is the Spark DataFrame containing data that is being read from MongoDB.

# Read customer data from a MongoDB collection into a Spark DataFrame
mongo_df = (
    spark.read
         .format("mongodb")
         .option("spark.mongodb.read.connection.uri", src_conn)
         .option("database", db_name)
         .option("collection", collection_name)
         .load()
)

# Process only 100 records in the current batch as required by the exercise.
batch_df = mongo_df.limit(100)

# Write the processed records to a Delta table.
# Delta format provide reliable storage and also ACID properties
batch_df.write \
        .format("delta") \
        .mode("append") \
        .save("/mnt/delta/customers")
