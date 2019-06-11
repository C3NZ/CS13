"""
    Recursive problems
"""
#!python

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


def slow_permutation(array, left, right):
    """
        The slow permutation of a string. The runtime  is O(n*n!) where n
        is the the total number of elements within our array. This algorithm generates
        a 'permutation tree', where it swaps characters until it reaches the end of a string and then
        backtracks
    """
    if left == right:
        return ["".join(array)]
    else:
        total_permutations = []
        # Generate all permutations
        for i in range(left, right + 1):
            array[left], array[i] = array[i], array[left]
            total_permutations.extend(slow_permutation(array, left + 1, right))
            array[left], array[i] = array[i], array[left]
        return total_permutations


def really_slow_permutation(array verbose=False):
    """
        The faster way of doing a permutation
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
        if verbose:
            print(f"Leading char: {leading_char}")
            print(f"remaining_list: {remaining_list}")

        # Iteerate the all permutations of the remaining permutation list.
        for perm in really_slow_permutation(remaining_list):
            curr_perm.append([leading_char] + perm)

            if verbose:
                print(f"Current permutation: {curr_perm}")

    return curr_perm


def test_speed_of_permutation_funcs() -> None:
    """
        Test the speed of the permutation functions we've created
    """
    test_list = ["a", "b", "c"]

    result = timeit.timeit(
        lambda: slow_permutation(test_list, 0, len(test_list) - 1), number=10
    )
    print(f"Slow permutation result: {result:.5f} seconds\n")

    result = timeit.timeit(lambda: really_slow_permutation(test_list), number=10)
    print(f"Fast permutation result: {result:.5f} seconds\n")
    print(len(really_slow_permutation(test_list)))
    print(len(slow_permutation(test_list, 0, len(test_list) - 1)))


test_speed_of_permutation_funcs()


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
