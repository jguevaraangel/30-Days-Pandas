import pandas as pd 

"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
"""

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = np.where(
        (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M')),
        employees['salary'],
        0
    )
    return employees[['employee_id', 'bonus']].sort_values('employee_id')
