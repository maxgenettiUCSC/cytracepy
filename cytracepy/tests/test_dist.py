from cytracepy.dist import branch, trajectory
import pandas as pd
import numpy as np


focus = pd.DataFrame(
    [
        [1, 2, 3, 4, 5],
        [1, 2, 5, 2, 1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 2, 1],
    ]
)

query = pd.DataFrame(
    [
        [9, 2, 3, 4, 1],
        [1, 2, 5, 2, 3],
        [5, 7, 3, 2, 3],
        [1, 2, 3, 20, 3],
    ]
)

focus_cxb = pd.DataFrame(
    [
        [1, 4],
        [2, 3],
        [10, 10],
        [4, 1],
    ], columns = ["f_b0", "f_b1"]
)

query_cxb = pd.DataFrame(
    [
        [1, 4],
        [5, 15],
        [3, 2],
        [4, 10],
    ], columns = ["f_b0", "f_b1"]
)


q_markers_dict = {
    "f_b0" : [0,1,2,3],
    "f_b1" : [0,1,2,3],
}

f_markers_dict = {
    "f_b0" : [0,1,2],
    "f_b1" : [0,1,3],
}


def test_branch_self_is_zero():
    answer = branch(focus, focus)
    assert answer == 0


def test_branch_different_gt_zero():
    answer = branch(focus, query)
    assert answer > 0


def test_branch_symmetry():
    """[summary]
    """
    assert branch(focus, query) == branch(query, focus) 


def test_trajectory_symmetry():
    """Test for symmetry. Must have same markers.
    """
    t1= trajectory(
        query, focus,
        query_cxb, focus_cxb,
        q_markers_dict
    )
    t2 = trajectory(
        focus, query,
        focus_cxb, query_cxb,
        q_markers_dict
    )
    assert t1 == t2


def test_trajectory_different_markers_different():
    t1= trajectory(
        query, focus,
        query_cxb, focus_cxb,
        q_markers_dict
    )
    t2 = trajectory(
        focus, query,
        focus_cxb, query_cxb,
        f_markers_dict
    )

    assert t1 != t2


def test_trajectory_self_is_zero():
    answer = trajectory(
        focus, focus,
        focus_cxb, focus_cxb,
        f_markers_dict
    )
    assert answer == 0


def test_trajectory_different_gt_zero():
    answer = trajectory(
        focus, query,
        focus_cxb, query_cxb,
        f_markers_dict
    )
    assert answer > 0
