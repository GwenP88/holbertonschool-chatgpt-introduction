#!/usr/bin/python3
import sys

def factorial(n):
    """
    factorial - Computes the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The number to compute the factorial for. Must be >= 0.

    Returns:
        int: The factorial of n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
