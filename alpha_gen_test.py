import pandas as pd
import numpy as np
from Alpha_Gen.aroon_indicator_alpha_gen import aroon_alpha_gen
from Alpha_Gen.mean_rev_1_alpha_gen import mr1_alpha_gen
from Asset_Alloc.quantymacro_allocator import quantymacro_allocator
from Asset_Alloc.wq_allocator import wq_allocator

LAG_DAYS = 3

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
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7], 
    [9, 8, 7, 6, 5],
    [3, 4, 5, 6, 7],
    [5, 4, 3, 2, 1], 
    [1, 2, 3, 4, 5],
    [7, 6, 5, 4, 3],
    [7, 8, 9 , 10 ,11],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5]], 
    index=date_array, 
    columns = ["Col_0","Col_1","Col_2","Col_3","Col_4"])


print(df)
print(mr1_alpha_gen(df, LAG_DAYS))
print(quantymacro_allocator(mr1_alpha_gen(df, LAG_DAYS)))
print(wq_allocator(mr1_alpha_gen(df, LAG_DAYS)))
#print(aroon_alpha_gen(df, 3))
