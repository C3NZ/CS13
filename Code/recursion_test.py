#!python

import itertools
import math
import unittest

from recursion import (factorial, fast_permutation, really_slow_permutation,
                       slow_permutation)


class RecursionTest(unittest.TestCase):
    def test_factorial_with_small_integers(self):
        # factorial should return the product n*(n-1)*...*2*1 for n >= 0
        assert factorial(0) == 1  # base case
        assert factorial(1) == 1  # base case
        assert factorial(2) == 2 * 1
        assert factorial(3) == 3 * 2 * 1
        assert factorial(4) == 4 * 3 * 2 * 1
        assert factorial(5) == 5 * 4 * 3 * 2 * 1
        assert factorial(6) == 6 * 5 * 4 * 3 * 2 * 1
        assert factorial(7) == 7 * 6 * 5 * 4 * 3 * 2 * 1
        assert factorial(8) == 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
        assert factorial(9) == 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
        assert factorial(10) == 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

    def test_factorial_with_large_integers(self):
        assert factorial(15) == 1307674368000
        assert factorial(20) == 2432902008176640000
        assert factorial(25) == 15511210043330985984000000
        assert factorial(30) == 265252859812191058636308480000000

    def test_factorial_with_negative_integers(self):
        # factorial should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg="function undefined for n < 0"):
            factorial(-1)
            factorial(-5)

    def test_factorial_with_floating_point_numbers(self):
        # factorial should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg="function undefined for float"):
            factorial(2.0)
            factorial(3.14159)

    def test_permutation_functions_lengths(self):
        """
            permutation functions should generate the correct amount of permutations
        """

        # Slow permutation tests
        assert len(slow_permutation(["a", "b", "c"], 0, 3)) == math.factorial(3)
        assert len(slow_permutation(["a", "b", "c", "d"], 0, 4)) == math.factorial(4)
        assert len(slow_permutation(["a", "b", "c", "d", "e"], 0, 5)) == math.factorial(
            5
        )

        # Really slow permutation tests
        assert len(really_slow_permutation(["a", "b", "c"])) == math.factorial(3)

        assert len(really_slow_permutation(["a", "b", "c", "d"])) == math.factorial(4)
        assert len(
            really_slow_permutation(["a", "b", "c", "d", "e"])
        ) == math.factorial(5)

        # Really slow permutation tests
        assert len(fast_permutation(["a", "b", "c"], 3)) == math.factorial(3)

        assert len(fast_permutation(["a", "b", "c", "d"], 4)) == math.factorial(4)
        assert len(fast_permutation(["a", "b", "c", "d", "e"], 5)) == math.factorial(5)

    def test_permutation_outputs(self):
        """
            Test the outputs of the permutations to make sure that they're equal
        """
        test_list = ["a", "b", "c"]

        # Convert output list of permutations into tuples so we can place
        # them within a set to compare against pythons built in permutation tool
        perms = [tuple(perm) for perm in really_slow_permutation(test_list)]
        assert set(perms) == set(itertools.permutations(test_list))

        perms = [tuple(perm) for perm in slow_permutation(test_list, 0, len(test_list))]
        assert set(perms) == set(itertools.permutations(test_list))

        perms = [tuple(perm) for perm in fast_permutation(test_list, len(test_list))]
        assert set(perms) == set(itertools.permutations(test_list))

        # Decent sized list test
        test_list = ["a", "b", "c", "d", "e"]

        # Really slow permutation algorithm test
        perms = [tuple(perm) for perm in really_slow_permutation(test_list)]
        assert set(perms) == set(itertools.permutations(test_list))

        # slow permutation algorithm test
        perms = [tuple(perm) for perm in slow_permutation(test_list, 0, len(test_list))]
        assert set(perms) == set(itertools.permutations(test_list))

        # fast permutation algorithm test
        perms = [tuple(perm) for perm in fast_permutation(test_list, len(test_list))]
        assert set(perms) == set(itertools.permutations(test_list))

        # Decent sized list test
        test_list = ["a", "b", "c", "d", "e"]

        # Really slow permutation algorithm test
        perms = [tuple(perm) for perm in really_slow_permutation(test_list)]
        assert set(perms) == set(itertools.permutations(test_list))

        # slow permutation algorithm test
        perms = [tuple(perm) for perm in slow_permutation(test_list, 0, len(test_list))]
        assert set(perms) == set(itertools.permutations(test_list))

        # fast permutation algorithm test
        perms = [tuple(perm) for perm in fast_permutation(test_list, len(test_list))]
        assert set(perms) == set(itertools.permutations(test_list))


if __name__ == "__main__":
    unittest.main()
