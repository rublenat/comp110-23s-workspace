"""Units tests for the functions in the file 'utils'."""
__author__ = "730396580"

from exercises.ex05.utils import only_evens, concat, sub


def test_empty_list() -> None:
    """Edge case test to see if empty list is returned when list has no elements."""
    assert only_evens([]) == []


def test_mixture() -> None:
    """Use case test to see if only even elements are returned when elements are even and odd."""
    assert only_evens([1, 5, 4]) == [4]


def test_all_even() -> None:
    """Use case test to see if all elements in list are returned when all elements are even."""
    assert only_evens([4, 6, 8]) == [4, 6, 8]


def test_with_no_elements() -> None:
    """Edge case to test concat function when one list has no elements."""
    first_list: list[int] = []
    second_list: list[int] = [1, 2, 3]
    assert concat(first_list, second_list) == [1, 2, 3]


def test_with_many_elements() -> None:
    """Use case to test concat function with many elements."""
    first_list: list[int] = [1, 2, 3, 4, 5, 6]
    second_list: list[int] = [7, 8, 9, 10, 11, 12]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def test_with_random() -> None:
    """Use case to test if first list is followed by list two with random ordered elements."""
    first_list: list[int] = [1, 10, 23, 15]
    second_list: list[int] = [33, 7, 106]
    assert concat(first_list, second_list) == [1, 10, 23, 15, 33, 7, 106]


def test_no_list() -> None:
    """Edge case to test if empty list is returned if given list has no elements."""
    a_list: list[int] = []
    assert sub(a_list, 3, 4) == []


def test_many() -> None:
    """Use case to test if subset returned starts at start index and ends at stop index(non inclusive)."""
    a_list: list[int] = [1, 3, 6, 9, 10]
    assert sub(a_list, 0, 3) == [1, 3, 6]


def test_high_end_index() -> None:
    """Use case to test if subset will include last index if given stop index is greater than the length of the list."""
    a_list: list[int] = [1, 3, 5, 7]
    assert sub(a_list, 0, 5) == [1, 3, 5, 7]