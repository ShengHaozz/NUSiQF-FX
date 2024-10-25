import pandas as pd
import numpy as np
from aroon_indicator_alpha_gen import aroon_alpha_gen
from mean_rev_1_alpha_gen import mr1_alpha_gen

date_array = pd.to_datetime([
    "2015-01-01",
    "2015-01-02",
    "2015-01-03",
    "2015-01-04",
    "2015-01-05",
    "2015-01-06",
    "2015-01-07",
    "2015-01-08",
    "2015-01-09",
    "2015-01-10"
    ])
df = pd.DataFrame([
    [1,2],
    [3,4], 
    [5,6],
    [3,4],
    [1,2], 
    [1,2],
    [3,4],
    [7,8],
    [3,4],
    [1,2]], 
    index=date_array, 
    columns = ["Left", "Right"])

print(df)
print(mr1_alpha_gen(df, 3))
print(aroon_alpha_gen(df, 3))
