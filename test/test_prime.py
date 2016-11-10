#!/usr/bin/env python

from prog.prime_number import is_prime, prime_numbers

import unittest

class PrimeTestCase(unittest.TestCase):
    def test_negative_prime_number(self):
        self.assertEqual(prime_numbers(-5), "Cannot find prime for less than 2")

    def test_number_zero(self):
        self.assertEqual(prime_numbers(0), "Cannot find prime for less than 2")

    def test_number_one(self):
        self.assertEqual(prime_numbers(1), "Cannot find prime for less than 2")

    def test_prime_number_two(self):
        self.assertEqual(prime_numbers(2), [2])

    def test_integer_number(self):
        self.assertEqual(prime_numbers("5"), "Only integers allowed")

    def test_bool(self):
        self.assertEqual(prime_numbers(True), "Only integers allowed")
    
    def test_prime_number_eleven(self):
        self.assertEqual(prime_numbers(11), [2, 3, 5, 7, 11])

    def test_if_input_is_list(self):
        self.assertEqual(prime_numbers([]), "Only integers allowed")
    
    def test_number_is_last_digit_in_prime_list(self):
        self.assertEqual(prime_numbers(97)[-1], 97)