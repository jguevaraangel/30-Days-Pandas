import pandas as pd

"""
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
(emp_id, event_day, in_time) is the primary key (combinations of columns with unique values) of this table.
The table shows the employees' entries and exits in an office.
event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
in_time and out_time are between 1 and 1440.
It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.
"""

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    groupby = employees.groupby(['emp_id', 'event_day'])
    out = pd.DataFrame({
    'total_time': groupby.apply(lambda x: (x['out_time'] - x['in_time']).sum())
    })
    out = out.reset_index()
    return out.rename(columns={'event_day': 'day'})    
