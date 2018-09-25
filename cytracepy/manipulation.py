"""
Common matrix manipulation operations needed for comparing
branches and trajectories.
"""
import pandas as pd


def order(matrix, psuedotime):
    """Order the rows of a matrix by rank of psuedotime.
    
    Arguments:
        matrix (pandas DataFrame): samples x features (rows x cols) matrix
        psuedotime (pandas Series): Ordererable values indexed by the same row names of matrix.

    Returns:
       (pandas DataFrame): ordered samples x features (rows x cols) matrix
    """
    return(matrix.loc[psuedotime.sort_values().index])
    

def sliding_window_mean(matrix, window_size):
    """Transform a matrix by calclulating the means of a given window size across rows.
    
    Arguments:
        matrix (pandas DataFrame): samples x features (rows x cols) matrix
        window_size (int): number of samples to average over
    
    Returns:
        (pandas DataFrame): n_windows x features (rows x cols) matrix
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
    """Subset matricies down to an intersection of features.
    
    Arguments:
        query (pandas DataFrame): samples x feature (row x col) matrix
        reference (pandas DataFrame): samples x feature matrix (row x col) matrix
        features (list): column ids that are in query and reference
    
    Returns:
        (pd.DataFrame, pd.DataFrame): tuple of modified matrices
    """
    features = set(features)
    q_features = set(query.columns)
    r_features = set(reference.columns)
    both_have = q_features.intersection(r_features).intersection(features)
    both_have = list(both_have)
    return query[both_have], reference[both_have]