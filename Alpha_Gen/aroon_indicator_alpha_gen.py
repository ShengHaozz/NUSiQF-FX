import pandas as pd
import numpy as np

def aroon_alpha_gen(input_df: pd.DataFrame, lag_days: int, up: bool = True) -> pd.DataFrame:
    # alpha = -(close(today) - close(X_days_ago))/close(X_days_ago)
    # first column is datetime (index)
    # subsequent columns are values

    # lookback period includes the day itself
    # direction = 1 for aroon up, -1 for aroon down

    # aroon() generates new col from col
    def aroon(series: pd.Series) -> pd.Series:
        lag_delta = pd.Timedelta(days = lag_days)
        one_delta = pd.Timedelta(days = 1)
        new_dict = {}

        for day in series.index[lag_days-1:]:
            ref_series = series[day - lag_delta + one_delta : day]
            if up:
                extreme_day = ref_series.idxmax()
            else:
                extreme_day = ref_series.idxmin()
            p_extreme = (day - extreme_day).days
            au = (1 - (p_extreme/lag_days)) * 100
            new_dict[day] = au
        
        return pd.Series(new_dict)

    new_df = input_df.copy()
    new_df = new_df.apply(aroon)

    return new_df
    


