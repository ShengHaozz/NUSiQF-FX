import pandas as pd
import numpy as np

# quantymacro allocator

def quantymacro_allocator(alpha_df: pd.DataFrame, weights: pd.DataFrame = None, group: dict = None) -> pd.DataFrame:
    
    # default group
    if group == None:
        group = {
            'A': ['Col_0','Col_1','Col_2'],
            'B': ['Col_3','Col_4']
        }
    group_keys = list(group.keys())

    # if weights not specified then equal weights
    if weights == None:
        new_weights = alpha_df.copy().map(lambda x: 1)
    else:
        new_weights = weights.copy()
    
    new_df = alpha_df.copy()

    # get alpha of each group
    for grouping in group_keys:
        new_df[grouping] = alpha_df.loc[:, group[grouping]].mean(axis = 1)
    
    # set new column 'diff' to +1 if col 0 > col 1 otherwise -1
    new_df['diff'] = (new_df[group_keys[0]] - new_df[group_keys[1]]).apply(lambda x: x if not x else x // abs(x))

    print(new_df['diff'])
    print(new_weights.loc[:,group[group_keys[0]]])
    
    # set weights to long/short
    new_weights.loc[:,group[group_keys[0]]] = new_weights.loc[:,group[group_keys[0]]].mul(new_df['diff'], axis = 0)
    new_weights.loc[:,group[group_keys[1]]] = new_weights.loc[:,group[group_keys[1]]].mul((-1) * new_df['diff'], axis = 0)

    # neutralise
    new_weights = new_weights.apply(lambda x: x - x.mean(), axis = 1)

    # normalise
    new_weights = new_weights.div(new_weights.abs().sum(axis = 1), axis = 0)

    return new_weights


    
    
    

    


