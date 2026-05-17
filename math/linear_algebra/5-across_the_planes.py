#!/usr/bin/env python3
"""This module adds two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise and returns a new matrix."""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    result = []
    for i, j in zip(mat1, mat2):
        row = []
        for a, b in zip(i, j):
            row.append(a + b)
        result.append(row)
    return result
