import pandas as pd
import numpy as np

# worldquant allocator

def wq_allocator(alpha_df: pd.DataFrame) -> pd.DataFrame:

    new_df = alpha_df.copy()

    # neutralise
    new_weights = new_df.apply(lambda x: x - x.mean(), axis = 1)

    # normalise
    new_weights = new_weights.div(new_weights.abs().sum(axis = 1), axis = 0)

    return new_weights


    
    
    

    


