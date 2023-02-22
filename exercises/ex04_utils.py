"""EX04 - 'List' Utility Functions."""
__author__ = "730396580"


def all(given_list: list[int], given_number: int) -> bool:
    """Checks to see if all numbers in the list match the given number."""
    idx: int = 0

    if len(given_list) == 0:
        return False

    while idx < len(given_list):
        if given_list[idx] != given_number:
            return False
        idx += 1

    return True


def max(input: list[int]) -> int:
    """Returns maximum value in a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    idx: int = 0
    max_value = input[0]

    while idx < len(input):
        if input[idx] >= max_value:
            max_value = input[idx]
        idx += 1

    return max_value


def is_equal(given_list1: list[int], given_list2: list[int]) -> bool:
    """Checks to see if every element at every index is equal."""
    idx: int = 0

    if len(given_list1) != len(given_list2):
        return False

    while idx < (len(given_list1) or len(given_list2)):
        if given_list1[idx] != given_list2[idx]:
            return False
        idx += 1

    return True 