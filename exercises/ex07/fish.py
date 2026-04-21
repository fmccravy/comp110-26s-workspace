"""File for Fish class."""

__author__ = "730941956"


class Fish:
    """Representation of a Fish in the river."""

    age: int

    def __init__(self):
        """Initialize age to 0."""
        self.age = 0

    def one_day(self):
        """Increase age by 1."""
        self.age += 1
