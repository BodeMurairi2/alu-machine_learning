#!/usr/bin/env python3
"""
This module computes addition, substraction, multiplication and division
"""
import numpy as np

def np_elementwise(mat1:np.ndarray, mat2:np.ndarray):
    """
    This function adds, subs, mult, and divide
    """
    shape_1 = mat1.shape()
    shape_2 = mat2.shape()
    if shape_1 != shape_2:
        raise ValueError("Not the same shape")
    add_vector = mat1 + mat2
    sub_vector = mat1 - mat2
    if shape_1[1] != shape_2[0]:
        raise ValueError("number of columns in a is not equal to number of rows of b")
    mult_vector = mat1 * mat2
    div_vector = mat1 / mat2
    return (
        add_vector,
        sub_vector,
        mult_vector,
        div_vector
        )
