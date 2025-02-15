import numpy as np
import pandas as pd

# Define your legend dictionary
legend = {'Open': 0, 'High': 1, 'Low': 2, 'Close': 3, 'Vol': 4}

def get_filtered_dataframe(metric, currencies, convert_currencies, updated_currencies, start_date):
    # Initialize a dictionary to hold columns and dataframes for each metric
    fx_columns = [f'{metric} of {symbol}' for symbol in currencies]
    fx_dataframe = pd.DataFrame(columns=fx_columns)
    
    # Populate the DataFrame with data from CSV files for each currency
    for symbol in currencies:

        data = pd.read_csv(f'Data_Processing/{symbol}1440.csv', index_col=0, sep='\t', header=None)
        fx_dataframe[f'{metric} of {symbol}'] = data.iloc[:, legend[metric]].copy()

    # Apply conversion for specific currency pairs if needed
    if metric != 'Vol':  # Conversion applies to all metric except 'Vol' metric
        for symbol in convert_currencies:
            column_name = f'Close of {symbol}'
            if column_name in fx_dataframe.columns:
                fx_dataframe[column_name] = (1 / fx_dataframe[column_name])

    # Update column names to reflect the updated currency pairs
    updated_columns = [f'{metric} of {symbol}' for symbol in updated_currencies]
    fx_dataframe.columns = updated_columns

    # Filter the DataFrame starting from the specified start date
    filtered_dataframe = fx_dataframe.loc[start_date:].copy()

    # Forward-fill any missing values
    filtered_dataframe.ffill(inplace=True)

    return filtered_dataframe