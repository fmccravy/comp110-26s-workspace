"""Unit tests for dictionary utility functions."""

__author__ = "730941956"

from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)
import pytest


# --- invert Tests ---


def test_invert_use_case_simple() -> None:
    """Test invert with a simple dictionary."""
    assert invert({"apple": "fruit", "carrot": "veggie"}) == {
        "fruit": "apple",
        "veggie": "carrot",
    }


def test_invert_use_case_long() -> None:
    """Test invert with multiple entries."""
    assert invert({"a": "1", "b": "2", "c": "3"}) == {"1": "a", "2": "b", "3": "c"}


def test_invert_edge_case_keyerror() -> None:
    """Test that invert raises KeyError when duplicate values become duplicate keys."""
    with pytest.raises(KeyError):
        # This matches the example from the assignment writeup
        my_dictionary = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(my_dictionary)


# --- count Tests ---


def test_count_use_case_standard() -> None:
    """Test count with various repeated items."""
    assert count(["apple", "apple", "banana"]) == {"apple": 2, "banana": 1}


def test_count_use_case_no_repeats() -> None:
    """Test count where every item is unique."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_edge_case_empty() -> None:
    """Test count with an empty list."""
    assert count([]) == {}


# --- alphabetizer Tests ---


def test_alphabetizer_use_case_basic() -> None:
    """Test alphabetizer with a standard list of words."""
    assert alphabetizer(["apple", "cat", "ant"]) == {
        "a": ["apple", "ant"],
        "c": ["cat"],
    }


def test_alphabetizer_use_case_already_sorted() -> None:
    """Test alphabetizer when list is already in order."""
    assert alphabetizer(["bat", "bear", "zebra"]) == {
        "b": ["bat", "bear"],
        "z": ["zebra"],
    }


def test_alphabetizer_edge_case_case_sensitivity() -> None:
    """Test alphabetizer ensures 'A' and 'a' are grouped together and lowercased."""
    # Your dictionary.py must use .lower() for this to pass
    assert alphabetizer(["Apple", "apple"]) == {"a": ["apple", "apple"]}


# --- favorite_color Tests ---


def test_favorite_color_use_case_majority() -> None:
    """Test favorite_color with a clear winner."""
    assert favorite_color({"Faith": "blue", "Craig": "blue", "Son": "green"}) == "blue"


def test_favorite_color_use_case_tie() -> None:
    """Test favorite_color where the first appearing color wins a tie."""
    assert favorite_color({"Faith": "blue", "Craig": "green"}) == "blue"


def test_favorite_color_edge_case_empty() -> None:
    """Test favorite_color with an empty dictionary."""
    assert favorite_color({}) == ""


# --- update_attendance Tests ---


def test_update_attendance_use_case_new_entry() -> None:
    """Test update_attendance when adding a new person on a new day."""
    attendance: dict[str, list[str]] = {"Monday": ["Faith"]}
    update_attendance(attendance, "Tuesday", "Craig")
    assert attendance == {"Monday": ["Faith"], "Tuesday": ["Craig"]}


def test_update_attendance_use_case_existing_day() -> None:
    """Test update_attendance adding a second person to an existing day."""
    attendance: dict[str, list[str]] = {"Monday": ["Faith"]}
    update_attendance(attendance, "Monday", "Craig")
    assert attendance == {"Monday": ["Faith", "Craig"]}


def test_update_attendance_edge_case_duplicate() -> None:
    """Test update_attendance does not add the same person to the same day twice."""
    # Your dictionary.py must check 'if student not in list' for this to pass
    attendance: dict[str, list[str]] = {"Monday": ["Faith"]}
    update_attendance(attendance, "Monday", "Faith")
    assert attendance == {"Monday": ["Faith"]}
