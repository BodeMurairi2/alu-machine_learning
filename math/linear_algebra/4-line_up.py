#!/usr/bin/env python3

"""
This module adds two list(element wise)
"""

def add_arrays(arr1, arr2):
    """
    This function adds two arrays
    Args:
        arr1:List[float|int]
        arr2:List[float|int]
    return
        arr3:List[float|int]
    """
    row_a = len(arr1)
    row_b = len(arr2)
    arr3 = []
    if row_a != row_b:
        return None

    if not isinstance(arr1[0], list) and not isinstance(arr2[0], list):
        for i, j in zip(arr1, arr2):
            arr3.append(i + j)
        return arr3

    dim_a = [row_a, len(arr1[0])]
    dim_b = [row_b, len(arr2[0])]

    if dim_a != dim_b:
        return None

    for i, j in zip(arr1, arr2):
        arr3.append([a + b for a, b in zip(i, j)])
    return arr3
