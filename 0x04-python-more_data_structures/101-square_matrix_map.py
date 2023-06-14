#!/usr/bin/python3
def matrix_square_map(matrix=[]):
    new_matrix = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
