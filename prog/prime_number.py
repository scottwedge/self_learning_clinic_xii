#!/usr/bin/env python

def is_prime(x):
    """
    Function to check if a number is prime
    """
    p_status = True
    if x < 2:
        p_status = False
    elif x == 2:
        p_status = True
    else:
        for i in range(2, x):
            if x % i == 0:
                p_status = False
    return p_status

def prime_numbers(n):
    """
    Generate prime numbers from 0 to n
    """
    primes = []
    if isinstance(n, bool):
        return "Only integers allowed"
    if not isinstance(n, int):
        return "Only integers allowed"
    if n < 2:
        return "Cannot find prime for less than 2"
    for y in range(1, n + 1):
        if is_prime(y):
            primes.append(y)
    return primes
