#!/usr/bin/env python3
"""
This module compute matrice multiplication
"""
import numpy as np


def np_matmul(mat1: np.ndarray, mat2: np.ndarray):
    """
    compute matrice multplication
    """
    try:
        mat3 = np.matmul(mat1, mat2)
        return mat3
    except Exception as error:
        raise error
