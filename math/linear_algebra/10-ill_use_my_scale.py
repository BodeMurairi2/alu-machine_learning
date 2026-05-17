#!/usr/bin/env python3
"""
This module returns the shape of nd.array
"""


import numpy as np


def np_shape(matrix: np.ndarray) -> tuple:
    """
    This function returns the shape of an array
    matrix:np.array
    return tuple
    """
    return np.shape(matrix)
