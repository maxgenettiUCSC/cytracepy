"""
Distance functions for pairs of trajectories.
"""
from scipy.spatial.distance import cosine
import pandas as pd
from fastdtw import fastdtw
import numpy as np
from cytracepy._checks import same_n_cols
from cytracepy.manipulation import sliding_window_mean, marker_intersection, order


@same_n_cols
def branch(focus, query, dist=cosine):
    """Branch distance calculated by dynamic time warping. 
    

    Note: This function assumes the rows are ordered by time, and that each row
        represents the same time interval.


    Args:
        focus (pandas DataFrame): ordered n_windows x n_features 
        query (pandas DataFrame): ordered n_windows x n_features  
        dist (callable):  function f(x, y) to calculate the distance between window vectors. Defaults to scipy.spatial.distance.cosine
    

    Returns:
        distance (float)
    """
    
    distance, path = fastdtw(focus, query, dist=dist)
    return distance


def greedy_min(branches_dist):
    """Return a single distance for a pair of trajectories from a branches distance matrix.
    
    Note: This is the default "condense" function for the trajectorty distance function.
    
    Args:
        branches_dist {pandas DataFrame} -- [focus_branches x query_branches]

    Returns:
        distance (float)   
    """
    return np.min(branches_dist).min()


def none(x):
    return x


def trajectory(
    focus, query,
    focus_cxb, query_cxb,
    markers,
    comparable=marker_intersection,
    dist=cosine,
    condense=greedy_min,
    smooth=none):
    """Return a distance measure between two trajectories.
    
    Arguments:
        focus (pandas DataFrame): cell ids x n_features, expression matrix 
        query (pandas DataFrame): cell ids x n_features, expression matrix
        focus_cxb (pandas DataFrame): cell ids x branch, branch ordering 
        query_cxb (pandas DataFrame): cell ids x branch, branch ordering
        markers (dict): branch ids in focus_cxb pointing a a list of features in focus and query
        comparable (callable): f(focus, query, marker_list) a function that makes focus and query comparable by giving them the same features. Defaults to cytracepy.manipulation.marker_intersection
        dist (callable):  f(x, y) to calculate the distance between window vectors. Defaults to scipy.spatial.distance.cosine
        condense (callable) -- f(branches_distance_matrix) derives a single distance measure from a matrix of branch distances. Defaults to cytracepy.dist.greedy_min
        smooth (callable) -- f(query) transforms the rows of cells into rows of comparable windows. Defaults to lambda x: return x.
    
    Returns:
        distance (float), return type of condense function
    """

    
    focus_branch_names = focus_cxb.columns
    query_branch_names = query_cxb.columns

    branches_distance = []
    for f_branch_name in focus_branch_names:
        branch_distance = []
        features = markers[f_branch_name]
        focus_subset, query_subset = comparable(
            focus, query, features
        )
        # Psuedotime for the focussed branch.
        f_psuedotime = focus_cxb[f_branch_name].dropna()
        focus_subset_tmp = focus_subset.loc[f_psuedotime.index]
        focus_subset_tmp = order(focus_subset_tmp, f_psuedotime)
        focus_subset_tmp = smooth(focus_subset_tmp)
        
        for q_branch_name in query_branch_names:
            
            q_psuedotime = query_cxb[q_branch_name].dropna()
            query_subset_tmp = query_subset.loc[q_psuedotime.index]
            query_subset_tmp = order(query_subset_tmp, q_psuedotime)
            query_subset_tmp = smooth(query_subset_tmp)
            distance = branch(focus_subset_tmp, query_subset_tmp)
            branch_distance += [ distance ]
        
        branches_distance.append(branch_distance)
    
    branches_dist = pd.DataFrame(branches_distance, columns=query_branch_names, index=focus_branch_names)
    distance = condense(branches_dist)
    return distance
