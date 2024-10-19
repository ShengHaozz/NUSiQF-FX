import pandas as pd
import numpy as np
from mean_rev_1_alpha_gen import mr1_alpha_gen

df = pd.DataFrame([[1,2],[3,4], [5,6],[7,8]], index=[0,1,2,3])
print(df)
print(mr1_alpha_gen(df, 2))
