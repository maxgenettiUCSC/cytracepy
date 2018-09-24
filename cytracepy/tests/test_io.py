from cytracepy.io import read_cell_x_branch, read_feature_matrix, read_markers
import io
import pandas as pd

feature_matrix = "\ta\tb\tc\n" +\
                 "1\t1\t2\t3\n" +\
                 "2\t1\t2\t3\n"

cell_x_branch = "b1\tb2\n" +\
                "1\t1\t.7\n" +\
                "2\t2.3\t5\n"

gmt = "b1\t\ta\tb\tc\n"+\
      "b2\t\td\tz\tf\t\n"

def test_gmt_is_dict():
    fh = io.StringIO(gmt)
    marker_dict = read_markers(fh)
    assert type(marker_dict) == dict

    
def test_gmt_keeps_order():
    fh = io.StringIO(gmt)
    marker_dict = read_markers(fh)
    assert marker_dict["b1"][1] == "b" 

def test_gmt_2():
    fh = io.StringIO(gmt)
    marker_dict = read_markers(fh)
    assert marker_dict["b2"][2] == "f" 

def test_cxb_is_dataframe():
    fh = io.StringIO(gmt)
    cxb = read_cell_x_branch(fh)
    assert type(cxb) == pd.DataFrame 

def test_feature_is_dataframe():
    fh = io.StringIO(gmt)
    fmat = read_feature_matrix(fh)
    assert type(fmat) == pd.DataFrame