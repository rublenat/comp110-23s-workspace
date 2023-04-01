"""EX08 - Wrangling Data."""
__author__ = "730396580"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV data into list of rows, each row as a dict[str, str]."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Produce a list of all values in a single column under the header (second parameter)."""
    result: list[str] = []

    for row in table:
        result.append(row[header])

    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform table as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]

    for key in first_row:
        result[key] = column_values(table, key)

    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only first N number of rows (second parameter)."""
    new_dictionary: dict[str, list[str]] = {}
    
    for key in table:
        values: list[str] = []
        for elements in table[key]:
            if len(values) < n:
                values.append(elements)
        new_dictionary[key] = values
    
    return new_dictionary


def select(table: dict[str, list[str]], column_interest: list[str]) -> dict[str, list[str]]:
    """Produce new table with only selected columns."""
    new_dictionary: dict[str, list[str]] = {}

    for column in table:
        idx: int = 0
        while idx < len(column_interest):
            if column == column_interest[idx]:
                new_dictionary[column] = table[column]
            idx += 1
    
    return new_dictionary


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based tbale with two column based tables combined."""
    new_dictionary: dict[str, list[str]] = {}

    for columns in table1:
        new_dictionary[columns] = table1[columns]
    
    for columns in table2:
        if columns in new_dictionary:
            new_dictionary[columns] += table2[columns]
        else:
            new_dictionary[columns] = table2[columns]
    
    return new_dictionary


def count(input: list[str]) -> dict[str, int]:
    """Given a list[str], counts the number of times each element in the list is present in the list."""
    new_dictionary: dict[str, int] = {}

    for item in input:
        if item in new_dictionary:
            new_dictionary[item] += 1
        else:
            new_dictionary[item] = 1
    
    return new_dictionary