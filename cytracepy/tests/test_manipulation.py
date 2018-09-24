from cytracepy.manipulation import order, marker_intersection
import pandas as pd


df = pd.DataFrame(
    [
        [1, 2, 3, 4, 5],
        [1, 2, 5, 2, 1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 2, 1],
    ], columns = ["c1","c2","c3","c4","c5"],
    index = ["i1","i2","i3","i4"],
)

def test_insection_maintain_order_first():
    reducedF, reducedQ = marker_intersection(df, df, ["c1", "c2"])
    assert reducedF.index[0] == "i1"


def test_insection_maintain_order_last():
    reducedF, reducedQ = marker_intersection(df, df, ["c1", "c2"])
    assert reducedF.index[3] == "i4"


def test_intersection():

    reducedF, reducedQ = marker_intersection(df, df, ["c1", "c2"])
    assert reducedF.shape[1] == reducedQ.shape[1]
    

def test_ordering_1():

    ordered = order(df, pd.Series([3,4,2,1], index = ["i1","i2","i3","i4"] ))
    assert ordered.index[0] == "i4"


def test_ordering_2():
    
    ordered = order(df, pd.Series([3,1,2,5], index = ["i1","i2","i3","i4"] ))
    assert ordered.index[0] == "i2"