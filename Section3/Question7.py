# Reading customer data from the CSV file.
# header=True uses the first row as column names.
# inferSchema=True automatically detects column data types.

customer_df = (
    spark.read
         .option("header", "true")
         .option("inferSchema", "true")
         .csv("/mnt/data/raw/customers.csv")
)

from pyspark.sql.functions import col, trim, upper

# Remove records where Customer_ID is null as i am cosidering Customer_ID to be a mandatory and unique field

cleaned_df = customer_df.dropna(subset=["Customer_ID"])

# Replace missing Age values with 0.

cleaned_df = cleaned_df.fillna({"Age": 0})

# Standardize City values by removing leading/trailing spaces
# and converting them to uppercase for consistency.

cleaned_df = cleaned_df.withColumn(
    "City",
    upper(trim(col("City")))
)

# Write the cleaned data to a Delta table.

cleaned_df.write \
          .format("delta") \
          .mode("overwrite") \
          .save("/mnt/delta/cleaned_customers")

