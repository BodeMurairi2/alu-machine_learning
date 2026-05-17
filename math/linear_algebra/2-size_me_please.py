#!/usr/bin/env python3


def matrix_shape(matrix: list) -> list:
    """
    Returns the shape of a matrix
    as a list of integers.
    Arg:
        matrix:list
    return []
    """
    shape = []
    current = matrix
    while type(current) is list:
        count = 0
        for i in current:
            count += 1
        shape.append(count)
        current = current[0]
    return shape
