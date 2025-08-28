import pandas as pd

"""
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

# solution 1 (optimal)
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars='product_id').rename(columns={'variable': 'store', 'value': 'price'}).dropna()  

# solution 2 using stack
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = products.set_index('product_id').stack().reset_index()
    result.columns = ['product_id', 'store', 'price']
    return result[result['price'].notna()]
