import pandas as pd

"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
"""

# solution 1 (not optimal)
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores['score'].sort_values(ascending=False)
    ranks = []
    temp_scores = []
    r = 0
    for score in sorted_scores:
        if score not in temp_scores:
            r += 1
        temp_scores.append(score)
        ranks.append(r)
    return pd.DataFrame({'score': sorted_scores, 'rank': ranks})

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    result = scores.copy()
    result['rank'] = scores['score'].rank(method='dense', ascending=False)
    return result[['score', 'rank']].sort_values('score', ascending=False)
