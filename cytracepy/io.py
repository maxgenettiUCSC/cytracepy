"""
Read functions for established trajectory related formats.
"""
from cytracepy._checks import filename_to_fileobj
import pandas as pd

@filename_to_fileobj
def read_cell_x_branch(file_like):
    """Get a cell x branch pandas dataframe.
    
    Args:
        cxb_lid {string} -- location identifyer
    """
    return pd.read_table(file_like, sep="\t", index_col=0)

@filename_to_fileobj
def read_feature_matrix(file_like):
    """Read a cell x branch pandas dataframe.
    
    Args:
        data_lid {string} -- location identifyer
        markers {list of string} -- constrict the returned matrix to these features.

    """
    return pd.read_table(file_like, sep="\t", index_col=0)

@filename_to_fileobj
def read_markers(file_like):
    """return a dictionary of branch ids pointing to lists of genes.
    
    Args:
        address {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """

    # Currently assumes gmt file.
    markers = {}
    
    for line in file_like:
        row = line.strip().split("\t")
        markers[row[0]] = row[2:]

    return markers