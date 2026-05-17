#!/usr/bin/env python3
"""
This module computes the transpose
of a 2D matrix.
"""


def matrix_transpose(matrix: list) -> list:
    """
    Returns the transpose of a 2D matrix.
    Args:
        matrix:list
    return transposed:list
    """
    transposed = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed
