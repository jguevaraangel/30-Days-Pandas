import pandas as pd

"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
"""

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee[['salary']].drop_duplicates().sort_values(by='salary', ascending=False)
    if len(unique_salaries) < 2:
        return pd.DataFrame({f'SecondHighestSalary': [None]})    
    second_salary = unique_salaries.iloc[[1]]
    return pd.DataFrame({f'SecondHighestSalary': [second_salary]})

