import pandas as pd

"""
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
"""

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    temp_df = orders.groupby('customer_number').count().reset_index()
    return temp_df[temp_df['order_number'] == temp_df['order_number'].max()][['customer_number']]    
