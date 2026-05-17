#!/usr/bin/env python3
"""This module slices a numpy array along specific axes."""


def np_slice(matrix, axes={}):
    """Slices a matrix along specific axes and returns a new numpy.ndarray."""
    slices = [slice(None)] * matrix.ndim
    for axis, s in axes.items():
        slices[axis] = slice(*s)
    return matrix[tuple(slices)]
