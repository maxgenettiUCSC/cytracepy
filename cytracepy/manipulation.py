"""
Common matrix manipulation operations needed for comparing
branches and trajectories.
"""
import pandas as pd

def order(matrix, psuedotime):
    """order the columns by rank
    
    Arguments:
        matrix {pandas data frame} -- [samples x features]
        rank {pandas series} -- series with ordererable values and names of the columns of matrix
    """
    return(matrix.loc[psuedotime.sort_values().index])
    

def sliding_window_mean(matrix, window_size):
    """[summary]
    
    Arguments:
        matrix {[type]} -- [description]
        window_size {[type]} -- [description]
    """

    smoothed = pd.DataFrame()
    start = 0
    end = start + window_size
    count = 1
    while end < matrix.shape[1]:
        smoothed["w" + str(count)] = matrix.iloc[:,start:end].mean(axis=1)
        count+=1
        start +=1
        end += 1

    return(smoothed) 


def marker_intersection(query, reference, features):
    """Subset the matrices down to their intersection of rows
    
    Arguments:
        query {pandas dataframe} -- [ samples x feature matrix ]
        reference {pandas dataframe} -- [ samples x feature matrix ]
    """
    features = set(features)
    q_features = set(query.columns)
    r_features = set(reference.columns)
    both_have = q_features.intersection(r_features).intersection(features)
    both_have = list(both_have)
    return query[both_have], reference[both_have]