"""Data related utility functions."""

__author__ = "730941956"

from csv import DictReader


def get_keys(input_dict: dict) -> list[str]:
    """Returns a list of all keys in a dictionary."""
    result: list[str] = []
    for key in input_dict:
        result.append(key)
    return result


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV file of data into a list of rows."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    if len(row_table) == 0:
        return result
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new table with only the first n rows of data."""
    result: dict[str, list[str]] = {}
    for column in table:
        first_n_items: list[str] = []
        for i in range(min(n, len(table[column]))):
            first_n_items.append(table[column][i])
        result[column] = first_n_items
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only a specific subset of columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = table[name]
    return result


def concat(
    table1: dict[str, list[str]], table2: dict[str, list[str]]
) -> dict[str, list[str]]:
    """Combine two column-based tables into one."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Count the frequency of each unique value in a list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert strings in selected columns to integers."""
    data_converted: dict[str, list[int | str]] = {}
    for col_name in data:
        data_converted[col_name] = []
        for value in data[col_name]:
            if col_name in columns_conv:
                data_converted[col_name].append(int(value))
            else:
                data_converted[col_name].append(value)
    return data_converted