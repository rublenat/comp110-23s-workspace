"""EX05 - 'List' utility functions."""
__author__ = "730396580"


def only_evens(given_list: list[int]) -> list[int]:
    """Returns only elements of the given list that are even."""
    evens_list: list[int] = list()
    idx: int = 0

    while idx < len(given_list):
        if given_list[idx] % 2 == 0:
            evens_list.append(given_list[idx])
        idx += 1

    return evens_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Generates a new list all elements in list1 followed by all elements of list2."""
    new_list: list[int] = list()
    idx: int = 0

    while idx < len(list1):
        new_list.append(list1[idx])
        idx += 1
    
    idx: int = 0
    while idx < len(list2):
        new_list.append(list2[idx])
        idx += 1
    
    return new_list


def sub(given_list: list[int], start_idx: int, stop_idx: int) -> list[int]:
    """Returns a subset of the given list starting from the start index and ending at the stop index - 1."""
    new_list: list[int] = list()

    if start_idx < 0:
        start_idx = 0
    if stop_idx > len(given_list):
        stop_idx = len(given_list)
    if (len(given_list) == 0) or (start_idx >= len(given_list)) or (stop_idx <= 0):
        return new_list
    
    while start_idx < stop_idx:
        new_list.append(given_list[start_idx])
        start_idx += 1

    return new_list