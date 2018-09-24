"""Chances to throw a meaningful error message."""
from functools import wraps
from decorator import decorator


@decorator
def filename_to_fileobj(func, *args, **kwargs):
    if type(args[0]) == str:
        args[0] = open(args[0], "r")

    return(func(*args, **kwargs))


@decorator
def same_n_cols(func, *args, **kwargs):
    if args[0].shape[1] != args[1].shape[1]:
        raise(
            ValueError(
                "n_features (n_samples, n_features) of " +\
                "first two arguments must be the same"
            )
        )

    return(func(*args, **kwargs))