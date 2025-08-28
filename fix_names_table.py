import pandas as pd

"""
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
"""

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.lower().str.capitalize()
    return users.sort_values(by='user_id') 
