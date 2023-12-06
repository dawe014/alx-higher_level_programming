#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = matrix.copy()
    for r in range(len(new_mat)):
        new_mat[r] = list(map(lambda x: x ** 2, new_mat[r]))
    return new_mat