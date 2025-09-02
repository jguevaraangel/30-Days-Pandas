import pandas as pd

"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
"""

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    grouped_df = employee.groupby('managerId')['name'].count().reset_index()
    print(grouped_df)
    return employee.merge(grouped_df[(grouped_df['name'] >= 5) | (grouped_df['name'] == 0)][['managerId']], left_on='id', right_on='managerId')[['name']]    
