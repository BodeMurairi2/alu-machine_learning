#!/usr/bin/env python3
"""This module adds two matrices of any number of dimensions."""


def add_matrices(mat1, mat2):
    """Adds two matrices element-wise and returns a new matrix."""
    if isinstance(mat1, list):
        if len(mat1) != len(mat2):
            return None
        result = []
        for a, b in zip(mat1, mat2):
            added = add_matrices(a, b)
            if added is None:
                return None
            result.append(added)
        return result
    return mat1 + mat2
