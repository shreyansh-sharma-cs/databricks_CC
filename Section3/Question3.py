#start_date and end_date are the input used to provide range during data extraction
#env tell whether we will be using dev or prod environment

dbutils.widgets.text("start_date", "")
dbutils.widgets.text("end_date", "")
dbutils.widgets.dropdown("env", "dev", ["dev", "prod"])

start_date = dbutils.widgets.get("start_date")
end_date = dbutils.widgets.get("end_date")
env = dbutils.widgets.get("env")

# Select the appropriate secret scope.

secret_scope = "mongodb.dev" if env == "dev" else "mongodb.prod"

# Retrieve MongoDB connection details.

src_conn = dbutils.secrets.get(scope=secret_scope, key="src_conn")
db_name = dbutils.secrets.get(scope=secret_scope, key="database")

# Read data from the MongoDB customers collection.

customer_df = (
    spark.read
         .format("mongodb")
         .option("spark.mongodb.read.connection.uri", src_conn)
         .option("database", db_name)
         .option("collection", "customers")
         .load()
)

# Extract records between the specified dates.

filtered_df = customer_df.filter(
    (col("Created_Date") >= start_date) &
    (col("Created_Date") <= end_date)
)

# Retrieve encryption key from Databricks Secret Scope.

secret_key = dbutils.secrets.get(
    scope="encryption",
    key="secret_key"
)

# Encrypt Customer_Name before writing to Delta.
# encrypt() represents an AES encryption function that uses secret_key.

encrypted_df = filtered_df.withColumn(
    "Customer_Name",
    encrypt(col("Customer_Name"), secret_key)
)

# Write encrypted data to Delta.

encrypted_df.write \
            .format("delta") \
            .mode("overwrite") \
            .save("/mnt/delta/sample_data")

# Decryption mechanism.
# decrypt() uses the same secret key to recover the original value.

decrypted_df = encrypted_df.withColumn(
    "Customer_Name",
    decrypt(col("Customer_Name"), secret_key)
)
