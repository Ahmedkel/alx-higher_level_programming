#!/usr/bin/python3
"""2-matrix_divided.py"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The number to divide by.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
            if each row of the matrix has a different size,
            or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix with each element divided by div,
        rounded to 2 decimal places.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    error_message_row_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(err_msg)

    matrix_row_length = 0

    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(err_msg)

        if matrix_row_length != 0 and len(row) != matrix_row_length:
            raise TypeError(error_message_row_size)

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err_msg)

        matrix_row_length = len(row)

    return [[round(i / div, 2) for i in row] for row in matrix]
