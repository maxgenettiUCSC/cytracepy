"""
Read functions for established trajectory related formats.
"""
from cytracepy._checks import filename_to_fileobj
import pandas as pd

@filename_to_fileobj
def read_cell_x_branch(fileobj):
    """Read cell x branch file into a pandas dataframe.
    
    Args:
        fileobj (string or file like object)
    
    Returns:
        (pandas DataFrame): cell x branch matrix
    """
    return pd.read_table(fileobj, sep="\t", index_col=0)

@filename_to_fileobj
def read_feature_matrix(fileobj, transpose=False):
    """Read an expression matrix into a pandas dataframe.

    Note: The matrix orientation expected by the package is cell-ids x gene-ids (rows x cols).
    
    Args:
        fileobj (string or file like object):  
        transpose (bool): whether to transpose
    
    Returns:
        (pandas DataFrame): expression matrix 
    """
    data = pd.read_table(fileobj, sep="\t", index_col=0)
    if transpose:
        data = data.transpose()
    
    return data

@filename_to_fileobj
def read_markers(fileobj):
    """Read a .gmt file into a branch->markers dictionary.
    
    Args:
       fileobj (string or file like object):
    
    Returns:
       (dict): branch-id -> markers dictionary
    """

    # Currently assumes gmt file.
    markers = {}
    
    for line in fileobj:
        row = line.strip().split("\t")
        markers[row[0]] = row[2:]

    return markers