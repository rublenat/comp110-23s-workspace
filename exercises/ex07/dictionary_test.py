"""Unit Tests for EX07."""
__author__ = "730396580"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_two() -> None:
    """Use case to see if inverts correctly when only two keys in dictonary."""
    assert invert({'Natalie': '20', 'Sarah': '21'}) == {'20': 'Natalie', '21': 'Sarah'}


def test_invert_many() -> None:
    """Use case to see if inverts correctly when mant keys in dictonary."""
    input: dict[str, str] = {'Natalie': '20', 'Sarah': '21', 'Isabella': '22', 'Kaylee': '23', 'Kim': '24', 'Kaleb': '25', 'Julia': '26'}
    assert invert(input) == {'20': 'Natalie', '21': 'Sarah', '22': 'Isabella', '23': 'Kaylee', '24': 'Kim', '25': 'Kaleb', '26': 'Julia'}


def test_no_dict() -> None:
    """Edge case to see if empty dictionary is returned when input is empty dictionary."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_keys_with_same_value() -> None:
    """Use case to see if first key in dictionary is returned if tie for most popular color."""
    input: dict[str, str] = {'Natalie': 'pink', 'Sarah': 'purple', 'Isabella': 'pink', 'Kim': 'purple'}
    assert favorite_color(input) == 'pink'


def test_many_colors() -> None:
    """Use test to see if correct color is returned when there is many colors."""
    input: dict[str, str] = {'Natalie': 'pink', 'Sarah': 'purple', 'Grayson': 'grey', 'Kim': 'pink', 'Quinnlan': 'pink', 'Kaylee': 'blue', 'Zach': 'pink', 'Emily': 'blue'}
    assert favorite_color(input) == 'pink'


def test_empty_dict() -> None:
    """Edge test to see if empty string is returned when dictionary is empty."""
    input: dict[str, str] = {}
    assert favorite_color(input) == ''


def test_count_few() -> None:
    """Use test to see if count is accurate with only a few elements in list."""
    input: list[str] = ['vanilla', 'chocolate', 'vanilla']
    assert count(input) == {'vanilla': 2, 'chocolate': 1}


def test_count_many() -> None:
    """Use test to see if count is accurate with many elements in list."""
    input: list[str] = ['vanilla', 'chocolate', 'vanilla', 'mint', 'cookie dough', 'chocolate', 'mint', 'vanilla', 'strawberry', 'mint']
    assert count(input) == {'vanilla': 3, 'chocolate': 2, 'mint': 3, 'cookie dough': 1, 'strawberry': 1}


def test_empty_count() -> None:
    """Edge test to see if empty dictionary is returned when input list is empty.""" 
    input: list[str] = []
    assert count(input) == {}