<<<<<<< HEAD
"""File for River class."""

__author__ = "730941956"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Representation of the river ecosystem."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """River and Bears."""
        self.day = 0
        self.fish = []
        self.bears = []
        for _ in range(num_fish):
            self.fish.append(Fish())
        for _ in range(num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish older than 3 and bears older than 5."""
        new_fish: list[Fish] = []
        for f in self.fish:
            if f.age <= 3:
                new_fish.append(f)
        self.fish = new_fish

        new_bears: list[Bear] = []
        for b in self.bears:
            if b.age <= 5:
                new_bears.append(b)
        self.bears = new_bears

    def remove_fish(self, amount: int):
        """Remove 'amount' many fish from the front of the list."""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)

    def bears_eating(self):
        """Bears eat 3 fish if at least 5 are present."""
        for b in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                b.eat(3)

    def check_hunger(self):
        """Remove bears with hunger_score < 0."""
        surviving_bears: list[Bear] = []
        for b in self.bears:
            if b.hunger_score >= 0:
                surviving_bears.append(b)
        self.bears = surviving_bears

    def repopulate_fish(self):
        """Each pair of fish produces 4 offspring."""
        offspring = (len(self.fish) // 2) * 4
        for _ in range(offspring):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Each pair of bears produces 1 offspring."""
        offspring = len(self.bears) // 2
        for _ in range(offspring):
            self.bears.append(Bear())

    def one_river_day(self):
        """Simulate one day in the river."""
        self.day += 1
        for f in self.fish:
            f.one_day()
        for b in self.bears:
            b.one_day()
        self.check_ages()
        self.check_hunger()
        self.bears_eating()
        self.repopulate_fish()
        self.repopulate_bears()

    def one_river_week(self):
        """Simulate seven days in the river."""
        for _ in range(7):
            self.one_river_day()

    def __str__(self) -> str:
        """String of river."""
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, r: "River") -> "River":
        """Combine two rivers."""
        return River(len(self.fish) + len(r.fish), len(self.bears) + len(r.bears))

    def __mul__(self, factor: int) -> "River":
        """Scale a river."""
        return River(len(self.fish) * factor, len(self.bears) * factor)
=======
"""File to define River class."""

from __future__ import annotations
from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        return None

    def bears_eating(self):
        return None

    def check_hunger(self):
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def __str__(self) -> str:
        return ""
    
    def __add__(self, other_riv: River) -> River:
        return self
    
    def __mul__(self, factor: int) -> River:
        return self

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)
>>>>>>> f17cfa5f9d1259c4558beefcebee05b458e0e434
