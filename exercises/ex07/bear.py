<<<<<<< HEAD
"""File for Bear class."""

__author__ = "730941956"


class Bear:
    """Representation of a Bear in the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize age and hunger_score to 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increase age by 1 and decrease hunger_score by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase hunger_score by the number of fish eaten."""
        self.hunger_score += num_fish
=======
"""File to define Bear class."""

class Bear:
    
    def __init__(self):
        return None
    
    def one_day(self):
        return None 
>>>>>>> f17cfa5f9d1259c4558beefcebee05b458e0e434
