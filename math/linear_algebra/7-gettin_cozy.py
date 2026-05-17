#!/usr/bin/env python3
"""
This module concatenates two 2D matrices
along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a given axis."""
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = []
        for row1, row2 in zip(mat1, mat2):
            result.append(row1[:] + row2[:])
        return result
    return None
