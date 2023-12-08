#!usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_num = lambda x : x ** 2
    return list(map(lambda x: list(map(square_num, x)), matrix))
