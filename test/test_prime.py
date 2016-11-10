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
        self.assertEqual(prime_numbers(2), 2)