#!/usr/bin/env python3
"""
This module computes addition, substraction, multiplication and division
"""


def np_elementwise(mat1, mat2):
    """
    This function adds, subs, mult, and divide
    """
    try:
        add_vector = mat1 + mat2
        sub_vector = mat1 - mat2
        mult_vector = mat1 * mat2
        div_vector = mat1 / mat2
    except Exception as error:
        raise error
    return (
        add_vector,
        sub_vector,
        mult_vector,
        div_vector
        )
