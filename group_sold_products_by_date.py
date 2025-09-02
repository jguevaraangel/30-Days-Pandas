import pandas as pd

"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
"""

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    num_sold = activities.drop_duplicates().groupby('sell_date').count().values
    products = activities.drop_duplicates().groupby('sell_date').agg({'product': lambda x: ','.join(sorted(x))}).reset_index().rename(columns={'product': 'products'})
    products['num_sold'] = num_sold
    return products[['sell_date', 'num_sold', 'products']]  
