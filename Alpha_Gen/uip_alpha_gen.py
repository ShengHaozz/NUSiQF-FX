import pandas as pd
import numpy as np

def uip_alpha_gen(input_df: pd.DataFrame):
    usd_df = 1 + input_df['USD']
    df = 1 + input_df.copy().drop(['USD'], axis = 1)
    print(usd_df.head())
    print(df.head())
    return df.div(usd_df, axis = 0)
