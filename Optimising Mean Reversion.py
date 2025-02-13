import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit

def compute_log_return(x, df):
    log_return_df = np.log(df / df.shift(x))
    
    # Compute mean & std across all currency pairs
    mean_log_return = log_return_df.mean().mean()  # Average across all columns
    std_log_return = log_return_df.std().mean()  # Average across all columns
    
    return log_return_df, mean_log_return, std_log_return

def optimize_lookback_cv(x_range, df, n_splits=5):
    tscv = TimeSeriesSplit(n_splits=n_splits) 
    results = {"x": [], "Mean CV Metric": []}
    best_x = None
    best_score = -np.inf
    
    for x in x_range:
        fold_metrics = []

        for train_idx, test_idx in tscv.split(df):
            train_df, test_df = df.iloc[train_idx], df.iloc[test_idx]
            _, mean_log_ret, std_log_ret = compute_log_return(x, train_df)
            
            # Define Sharpe-like metric
            metric = mean_log_ret / std_log_ret if std_log_ret > 0 else -np.inf
            fold_metrics.append(metric)

        # Compute average metric across folds
        avg_metric = np.mean(fold_metrics)
        results["x"].append(x)
        results["Mean CV Metric"].append(avg_metric)

        if avg_metric > best_score:
            best_x = x
            best_score = avg_metric

    results_df = pd.DataFrame(results)

    return best_x, results_df

# Example usage
x_range = range(2, 50)
n_splits = 5

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
    
optimal_x, results_df = optimize_lookback_cv(x_range, df, n_splits)



print(f"Optimal lookback period (x) from {n_splits}-fold CV: {optimal_x}")
