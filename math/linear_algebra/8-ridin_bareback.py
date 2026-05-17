#!/usr/bin/env python3
"""
This module computes matrix multiplication
"""


def matrix_mult(mat1, mat2):
    """Multiplies two matrices and returns the result as a new matrix."""
    if not mat1 or not mat2:
        raise ValueError("Input matrices cannot be empty")

    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])

    if cols_mat1 != rows_mat2:
        raise ValueError("mat1 columns must equal mat2 rows")

    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]

    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
