"""Lesson 22"""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as list of dict"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Return value in table under a certain header."""
    result: list[str] = []
    #strep through table
    for row in table:
    #save every value under the key "header"
        result.append(row[header])
    return result

def columnar(table: list[str, str]) -> dict[str, list[str]]:
    """Reforms data"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
    # for each key make a dictionary entry of all column values
        result[key] = column_vals(table, key)
    return result