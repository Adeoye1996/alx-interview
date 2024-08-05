#!/usr/bin/python3
'''
The python Module,
Given a number n, write a method that calculates the
fewest number of operations
'''


def minOperations(n):
    """
    Let calculates the fewest number of operations needed to result in
    n H characters
    """
    operations = 0
    min_operations = 2

    while n > 1:
        if (n % min_operations == 0):
            operations += min_operations
            n = n / min_operations
        else:
            min_operations += 1
    return (operations)
