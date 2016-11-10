#!/usr/bin/env python

def is_prime(x):
        p_status = True
        if x < 2:
            p_status = False
        else:
            for i in range(2,x):
                if x % i == 0:
                    p_status = False
        return p_status

def prime_numbers(n):
    """
    Generate prime numbers from 0 to n
    """
    if n < 2:
        return "Cannot find prime for less than 2"
    for y in range(1, n + 1):
        if is_prime(y):
            return(y)
print(prime_numbers(0))
print(prime_numbers(1))
print(prime_numbers(2))
print(prime_numbers(97))