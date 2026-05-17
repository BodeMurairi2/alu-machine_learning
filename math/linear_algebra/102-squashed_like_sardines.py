#!/usr/bin/env python3
"""This module concatenates two matrices along a specific axis."""


def get_shape(matrix):
    """Returns the shape of a matrix as a list of integers."""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + get_shape(matrix[0])


def deep_copy(matrix):
    """Returns a deep copy of a matrix."""
    if not isinstance(matrix, list):
        return matrix
    return [deep_copy(x) for x in matrix]


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two matrices along a given axis."""
    if axis == 0:
        s1 = get_shape(mat1[0]) if isinstance(mat1[0], list) else []
        s2 = get_shape(mat2[0]) if isinstance(mat2[0], list) else []
        if s1 != s2:
            return None
        return [deep_copy(x) for x in mat1] + [deep_copy(x) for x in mat2]
    if len(mat1) != len(mat2):
        return None
    result = []
    for a, b in zip(mat1, mat2):
        sub = cat_matrices(a, b, axis - 1)
        if sub is None:
            return None
        result.append(sub)
    return result
