"""
    Recursive problems
"""
#!python

import itertools
import math
import timeit


def factorial(n: int):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial is undefined for n = {}".format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_iterative(n)


def factorial_iterative(n: int) -> int:
    # TODO: implement the factorial function iteratively here
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests
    if n == 0:
        return 1

    factorial_sum = n

    # Iterate through all numbers and multiply our factorial
    for i in range(n - 1, 1, -1):
        factorial_sum *= i
    return factorial_sum


def factorial_recursive(n: int) -> int:
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def fast_permutation(array: list, k: int):
    """
        Fast permutation solution using Heaps algorithm.  Relies heavily
        on swapping values at indicies to generate the all permutations.
        https://en.wikipedia.org/wiki/Heap%27s_algorithm

        Arguments:
            array: The array  we're permutating
            k: the length of the array

        Returns:
            a list containing all of the permutations of the original array
    """
    if k == 1:
        return ["".join(array)]
    else:
        all_permutations = []
        all_permutations.extend(fast_permutation(array, k - 1))

        for i in range(k - 1):
            if k % 2 == 0:
                array[i], array[k - 1] = array[k - 1], array[i]
            else:
                array[0], array[k - 1] = array[k - 1], array[0]

            all_permutations.extend(fast_permutation(array, k - 1))

        return all_permutations


def slow_permutation(array, left, right):
    """
        The slow permutation of a string. The runtime  is O(n*n!) where n
        is the the total number of elements within our array. This algorithm generates
        a 'permutation tree', where it swaps characters until it reaches the end of a string and then
        backtracks
    """
    if left == right:
        # Return a copy of the array, as using array will just be the
        # one that we're swapping in memory
        return [array[:]]
    else:
        total_permutations = []
        # Generate all permutations
        for i in range(left, right):
            array[left], array[i] = array[i], array[left]
            total_permutations.extend(slow_permutation(array, left + 1, right))
            array[left], array[i] = array[i], array[left]

        return total_permutations


def really_slow_permutation(array, verbose=False):
    """
        The faster way of doing a permutation by using 
    """
    if not array:
        return []

    if len(array) == 1:
        return [array]

    curr_perm = []

    # Iterate through the current array
    for i in range(len(array)):
        # Grab the leading character
        leading_char = array[i]

        # Create the remaining list
        remaining_list = array[:i] + array[i + 1 :]

        # Output
        if verbose:
            print(f"Leading char: {leading_char}")
            print(f"remaining_list: {remaining_list}")

        # Iterate the all permutations of the remaining permutation list.
        for perm in really_slow_permutation(remaining_list):
            # Add the current permutation all up.
            curr_perm.append([leading_char] + perm)

            if verbose:
                print(f"Current permutation: {curr_perm}")

    return curr_perm


def generate_permutation(num_items: 3, use_letters: False):
    pass


def test_speed_of_permutation_funcs() -> None:
    """
        Test the speed of the permutation functions we've created
    """
    test_list = ["a", "b", "c", "d", "e"]

    # Custom, really slow permutation function
    result = timeit.timeit(lambda: really_slow_permutation(test_list), number=10)
    print(f"Really slow permutation result: {result:.5f} seconds\n")

    # Custom, somewhat slow permutation function
    result = timeit.timeit(
        lambda: slow_permutation(test_list, 0, len(test_list) - 1), number=10
    )
    print(f"Slow permutation result: {result:.5f} seconds\n")

    result = timeit.timeit(
        lambda: fast_permutation(test_list, len(test_list) - 1), number=10
    )
    print(f"Fast permutation result: {result:.5f} seconds\n")

    # Built in permutation function
    result = timeit.timeit(lambda: itertools.permutations(test_list), number=10)
    print(f"Built in permutation result: {result:.5f} seconds\n")


def main() -> None:
    import sys

    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print("factorial({}) => {}".format(num, result))
    else:
        print("Usage: {} number".format(sys.argv[0]))


if __name__ == "__main__":
    main()
