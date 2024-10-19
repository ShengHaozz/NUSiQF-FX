import pandas as pd
import numpy as np

def mr1_alpha_gen(input_df: pd.DataFrame, lag_days: int) -> pd.DataFrame:
    # alpha = -(close(today) - close(X_days_ago))/close(X_days_ago)
    # first column is datetime (index)
    # subsequent columns are values

    new_df = input_df.copy()
    new_df = new_df.pct_change(periods = lag_days)
    new_df = -new_df.iloc[lag_days:]

    return new_df
    


