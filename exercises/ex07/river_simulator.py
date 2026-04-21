"""File for running the River simulation."""

__author__ = "730941956"

from exercises.ex07.river import River

my_river: River = River(10, 2)
print(my_river)
my_river.one_river_week()
print(my_river)
