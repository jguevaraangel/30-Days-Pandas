import pandas as pd

"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
"""

# solution 1 (unoptimal)
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = 0
    average_salary = 0
    high_salary = 0

    for i in accounts['income']:
        if i < 20000:
            low_salary += 1
        elif i >= 20000 and i <= 50000:
            average_salary += 1
        else:
            high_salary += 1
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_salary, average_salary, high_salary]
    })

# solution 2 (np.select)
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    conditions = [
        accounts["income"] < 20000,
        accounts["income"].between(20000, 50000),
        accounts["income"] > 50000
    ]
    choices = ["Low Salary", "Average Salary", "High Salary"]

    accounts["category"] = np.select(conditions, choices)

    result = accounts["category"].value_counts().reindex(choices).reset_index()
    result.columns = ["category", "accounts_count"]

    return result
