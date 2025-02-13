import pandas as pd
import numpy as np

csvfilename = 'Data_Processing/Interest_Rates.csv'

def get_ir_df() -> pd.DataFrame:
    df = pd.read_csv(csvfilename, index_col = 'Date')
    df.index = pd.to_datetime(df.index, format= "%d/%m/%Y")
    df = df/100
    return df

# read_ir_csv("Data Processing/Interest_Rates.csv")