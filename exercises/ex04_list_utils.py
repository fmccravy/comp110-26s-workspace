"""ex04 - list utility functions."""

__author__ = "730941956"


def all(int_list: list[int], target: int) -> bool:
    """returns true if all #s match target, else false."""
    if len(int_list) == 0:
        return False

    for num in int_list:
        if num != target:
            return False

    return True


def max(input: list[int]) -> int:
    """returns largest num in list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")

    max_val: int = input[0]
    for num in input:
        if num > max_val:
            max_val = num

    return max_val


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """returns True if every element at every index is equal in both lists."""
    if len(list1) != len(list2):
        return False

    index: int = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """mutates list1 by appending list2 values to the end."""
    for item in list2:
        list1.append(item)
