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

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})    
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N > len(unique_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    nth_salary = unique_salaries.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]}) 
