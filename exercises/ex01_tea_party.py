"""Planning a cozy tea party"""

__author__: str = "730941956"


def main_planner(guests: int) -> None:
    """Entry point for the tea party planner."""

    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("tea bags: " + str(tea_bags(people=guests)))
    print("treats: " + str(treats(people=guests)))
    print(
        "cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """calculate the amount of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """1.5 treat per tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """finding cost of treats and tea."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?] ")))
