import pandas as pd

"""
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
"""

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    temp_df = courses.groupby('class')['student'].count().reset_index()
    return temp_df[temp_df['student'] >= 5][['class']]    
