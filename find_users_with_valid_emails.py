import pandas as pd

"""
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
"""

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    domain_check = users['mail'].str.endswith('@leetcode.com')
    prefix = users['mail'].str.replace('@leetcode.com', '', regex=False)
    starts_with_letter = prefix.str.match(r'^[a-zA-Z]')
    valid_characters = prefix.str.match(r'^[a-zA-Z0-9._-]+$')
    valid_condition = domain_check & starts_with_letter & valid_characters
    return users[valid_condition]    
