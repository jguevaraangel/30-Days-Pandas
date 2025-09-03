import pandas as pd

"""
Table: Candidates
+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| candidate_id | int      |
| name         | varchar  |
| years_of_exp | int      |
| interview_id | int      |
+--------------+----------+
candidate_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of a candidate, their number of years of experience, and their interview ID.

Table: Rounds
+--------------+------+
| Column Name  | Type |
+--------------+------+
| interview_id | int  |
| round_id     | int  |
| score        | int  |
+--------------+------+
(interview_id, round_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the score of one round of an interview.
"""

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    candidates = candidates[candidates["years_of_exp"]>=2]

    rounds = rounds.merge(candidates, how="left")

    rounds = rounds.groupby(["candidate_id"])[["score"]].sum().reset_index()

    rounds = rounds[rounds["score"]>15]

    return rounds[["candidate_id"]]
