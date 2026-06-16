-- Here we are first exposing the MongoDB collection as a dataframe and then creating a temp view from it. This allows us to run SQL queries on the MongoDB data.

-- customer_df = (
--     spark.read
--         .format("mongodb")
--         .option("spark.mongodb.read.connection.uri", src_conn)
--         .option("database", db_name)
--         .option("collection", "customers")
--         .load()
-- )

-- # Expose MongoDB data as a SQL view
-- customer_df.createOrReplaceTempView("customers_view")

CREATE OR REPLACE TABLE customer_age_stats
USING DELTA
LOCATION '/mnt/delta/customer_age_stats'
AS
SELECT
    City,
    AVG(Age) AS average_age,
    MIN(Age) AS minimum_age,
    MAX(Age) AS maximum_age
FROM customers_view
GROUP BY City;

-- customers_view is a temp view with customer data
-- read from the MongoDB "customers" collection.

-- The Delta table customer_age_stats will store the aggregated
-- customer age statistics for each city.

-- AVG(Age) calculates the average age of customers
-- MIN(Age) returns the minimum customer age 
-- MAX(Age) returns the maximum customer age 

-- result stored in delta format at the specified location


