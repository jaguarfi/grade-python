import unittest

from hypothesis import given, strategies, settings

# Use a model solution to check the correct behaviour for the submitted file
from model import is_prime as model_is_prime
from primes import is_prime


class TestPrimesGrader(unittest.TestCase):
    def test_is__prime_with_small_set(self):
        """is_prime returns True for prime numbers and False for non-prime numbers in range(100, 200)."""

        for i in range(100, 200):
            if model_is_prime(i):
                self.assertTrue(
                    is_prime(i),
                    "{} is a prime number but your function says it is not.".format(i)
                )
            else:
                self.assertFalse(
                    is_prime(i),
                    "{} is not a prime number but your function says it is.".format(i)
                )

    # Generate random integers in range(0, 10**6 + 1) and pass them
    # as parameter 'i' to the test method.
    @given(strategies.integers(0, 10**5))
    @settings(max_examples=1000, database=None, max_shrinks=1)
    def test_is__prime_with_large_set(self, i):
        """is_prime returns True for prime numbers and False for non-prime numbers for 1000 random positive integers in range(0, 10**6)."""

        if model_is_prime(i):
            self.assertTrue(
                is_prime(i),
                "{} is a prime number but your function says it is not.".format(i)
            )
        else:
            self.assertFalse(
                is_prime(i),
                "{} is not a prime number but your function says it is.".format(i)
            )
