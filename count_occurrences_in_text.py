import pandas as pd

"""
Table: Files
+-------------+---------+
| Column Name | Type    |
+-- ----------+---------+
| file_name   | varchar |
| content     | text    |
+-------------+---------+
file_name is the column with unique values of this table. 
Each row contains file_name and the content of that file.
"""

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    files["bull"] = np.where(files["content"].str.contains(" bull "), 1, 0)
    files["bear"] = np.where(files["content"].str.contains(" bear "), 1, 0)

    output = pd.DataFrame(files[["bull", "bear"]].sum().reset_index())
    output = output.rename(columns={"index": "word", 0: "count"})

    return output
