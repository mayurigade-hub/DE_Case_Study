import pandas as pd

data = {
    "date": [
        "2025-01-10", "2025-01-15",
        "2025-02-05", "2025-02-15",
        "2025-03-10", "2025-03-20",
        "2025-04-05", "2025-04-15"
    ],
    "city": [
        "Mumbai", "Pune",
        "Mumbai", "Nashik",
        "Pune", "Mumbai",
        "Nashik", "Pune"
    ],
    "category": [
        "Electronics", "Electronics",
        "Furniture", "Electronics",
        "Furniture", "Electronics",
        "Furniture", "Electronics"
    ],
    "product": [
        "Laptop", "Mobile",
        "Chair", "Laptop",
        "Table", "Mobile",
        "Chair", "Laptop"
    ],
    "quantity": [2, 5, 10, 3, 4, 8, 6, 2],
    "sales": [
        120000, 75000, 30000, 180000,
        40000, 120000, 18000, 120000
    ]
}

df = pd.DataFrame(data)

df.to_parquet("sales.parquet", index=False)

print("Parquet file created successfully!")