import pandas as pd

"""
Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.

"""

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store = store[store["amount"]>500]
    return pd.DataFrame({"rich_count": [len(store["customer_id"].unique())]})
