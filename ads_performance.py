import pandas as pd

"""
Table: Ads
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| ad_id         | int     |
| user_id       | int     |
| action        | enum    |
+---------------+---------+
(ad_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the ID of an Ad, the ID of a user, and the action taken by this user regarding this Ad.
The action column is an ENUM (category) type of ('Clicked', 'Viewed', 'Ignored').
"""

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ctr = ads.groupby('ad_id')['action'].apply(
        lambda x: round(
            (sum(x == 'Clicked') / (sum(x == 'Clicked') + sum(x == 'Viewed')) * 100) if (sum(x == 'Clicked') + sum(x == 'Viewed')) > 0 else 0.00, 
            2
        )
    ).reset_index()

    ctr.columns = ['ad_id', 'ctr']
    
    result = ctr.sort_values(by=['ctr', 'ad_id'], ascending=[False, True])

    return result
