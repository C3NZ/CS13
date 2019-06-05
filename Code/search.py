#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """
        Iterative linear search function -> O(n) runtime
    """
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """
        Recursive linear search function -> O(n) runtime
    """
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if len(array) - 1 < index:
        return None
    if item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index=index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """
        Iterative Binary search function -> O(logn) runtime
    """
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    # Setup the initial variables
    left = 0
    right = len(array) - 1
    mid = (right - left) // 2

    # While the left side is less than or equal to the right...
    while left <= right:

        if array[mid] == item:
            return mid
        elif array[mid] > item:
            right = mid - 1
        else:
            left = mid + 1

        # Get the new midpoint (in between the left and right side)
        mid = (left + right) // 2
    return None


def binary_search_recursive(array, item, left=None, right=None):
    """
        Recursive Binary search function -> O(logn) runtime
    """
    # TODO: implement binary search recursively here
    if left is None:
        starting_left = 0
        starting_right = len(array) - 1
        mid = (starting_right - starting_left) // 2

        if array[mid] == item:
            return mid
        elif array[mid] > item:
            new_right = mid - 1
            return binary_search_recursive(
                array, item, left=starting_left, right=new_right
            )
        else:
            new_left = mid + 1
            return binary_search_recursive(
                array, item, left=new_left, right=starting_right
            )
    elif right < left:
        return None
    elif left <= right:
        mid = (left + right) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            new_right = mid - 1
            return binary_search_recursive(array, item, left=left, right=new_right)
        else:
            new_left = mid + 1
            return binary_search_recursive(array, item, left=new_left, right=right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
