import pandas as pd

"""
Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.

 

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.

 

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

"""

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    two_df = students.merge(subjects, how='cross')
    
    exam_count = examinations.groupby(['student_id', 'subject_name']).agg(
        attended_exams=('subject_name', 'count')
    ).reset_index()
    
    all_df = two_df.merge(exam_count, on=['student_id','subject_name'], how='left').sort_values(by = ['student_id', 'subject_name'])
    all_df['attended_exams'] = all_df['attended_exams'].fillna(0)
    return all_df[['student_id', 'student_name', 'subject_name', 'attended_exams']]    
