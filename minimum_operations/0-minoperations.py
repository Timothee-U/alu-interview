#!/usr/bin/python3
"""The single character H appears in a text file.  
There are just two things your text editor can do with this file: 
Copy All and Paste. 
 Write a method that, given a number n,
determines the minimum number of operations required to produce

 The file contains precisely n H characters."""


def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
