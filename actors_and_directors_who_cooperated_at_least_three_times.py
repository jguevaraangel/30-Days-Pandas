import pandas as pd

"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
"""

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped_df = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()
    return grouped_df[grouped_df['timestamp'] >= 3][['actor_id', 'director_id']]
    
