#!/usr/bin/python3

"""
This module contains a pascal triangle function
"""


def pascal_triangle(n):
    """
    This function returns an array representation
    of a pascal triangle of length n
    """

    size = 2
    temp = list()
    result = list()
    result.append([1])

    if (n <= 0):
        return ([])

    if (n == 1):
        return (result)

    result.append([1, 1])

    for i in range(n - 2):
        size += 1
        temp = [1]
        for j in range(1, size - 1):
            temp.append(result[-1][j] + result[-1][j - 1])

        temp.append(1)
        result.append(temp)

    return (result)
