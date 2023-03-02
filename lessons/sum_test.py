"""Unit test for sum function"""

from lessons.sum import sum

def test_empty() -> None:
    assert sum([]) == 0.0

def test_one_element() -> None:
    assert sum([1.0]) == 1.0

def test_many() -> None:
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert sum(test_list) == 6.0

def test_negative() -> None:
    test_list: list[float] = [-1.0, 1.0, 2.0]
    assert sum(test_list) == 2.0

x = 1
def f(y: int) -> int:
    return x + y

print(f(x + 1))
