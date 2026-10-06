import duckdb

con = duckdb.connect()

# 1. Display Parquet data
print("\n--- ORIGINAL PARQUET DATA ---")

print(con.execute("""
    SELECT *
    FROM 'sales.parquet'
""").fetchdf())


# 2. ROLL-UP
# Total sales by category
print("\n--- ROLL-UP: SALES BY CATEGORY ---")

print(con.execute("""
    SELECT
        category,
        SUM(sales) AS total_sales
    FROM 'sales.parquet'
    GROUP BY category
    ORDER BY category
""").fetchdf())


# 3. DRILL-DOWN
# Category -> Product
print("\n--- DRILL-DOWN: CATEGORY AND PRODUCT ---")

print(con.execute("""
    SELECT
        category,
        product,
        SUM(sales) AS total_sales
    FROM 'sales.parquet'
    GROUP BY category, product
    ORDER BY category, product
""").fetchdf())


# 4. SLICE
# Only Electronics
print("\n--- SLICE: ELECTRONICS ---")

print(con.execute("""
    SELECT *
    FROM 'sales.parquet'
    WHERE category = 'Electronics'
""").fetchdf())


# 5. DICE
# Mumbai + Electronics
print("\n--- DICE: MUMBAI + ELECTRONICS ---")

print(con.execute("""
    SELECT *
    FROM 'sales.parquet'
    WHERE city = 'Mumbai'
      AND category = 'Electronics'
""").fetchdf())


# 6. AGGREGATION
print("\n--- AGGREGATION ---")

print(con.execute("""
    SELECT
        SUM(sales) AS total_sales,
        AVG(sales) AS average_sales,
        MAX(sales) AS maximum_sales,
        MIN(sales) AS minimum_sales,
        SUM(quantity) AS total_quantity
    FROM 'sales.parquet'
""").fetchdf())


# 7. SALES BY CITY
print("\n--- SALES BY CITY ---")

print(con.execute("""
    SELECT
        city,
        SUM(sales) AS total_sales
    FROM 'sales.parquet'
    GROUP BY city
    ORDER BY total_sales DESC
""").fetchdf())


con.close()