import pandas as pd

"""
| name        | continent | area    | population | gdp          |
| ----------- | --------- | ------- | ---------- | ------------ |
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
"""

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filtered_table = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return filtered_table[['name', 'population', 'area']]    
