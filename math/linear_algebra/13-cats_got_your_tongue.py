#!/usr/bin/env python3
"""This module concatenates two numpy arrays along a specific axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two matrices along a given axis and returns a new array."""
    return np.concatenate((mat1, mat2), axis=axis)
