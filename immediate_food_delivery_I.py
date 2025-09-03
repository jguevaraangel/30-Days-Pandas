import pandas as pd

"""
Table: Delivery
+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key (column with unique values) of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
"""

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery["immediate"] = np.where(delivery["order_date"] == delivery["customer_pref_delivery_date"], 1, 0)
    return pd.DataFrame({"immediate_percentage": [np.round((delivery["immediate"].mean()*100), 2)]})
