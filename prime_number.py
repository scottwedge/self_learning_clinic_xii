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
    for y in range(1,n+1):
        if is_prime(y):
            print(y)
prime_numbers(0)
prime_numbers(1)
prime_numbers(2)
prime_numbers(97)