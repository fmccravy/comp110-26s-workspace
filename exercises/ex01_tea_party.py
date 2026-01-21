"""Planning a cozy tea party"""

__author__: str = "730941956"


def main_planner(guests: int) -> None:
    """Entry point for the tea party planner."""

    tea_count = tea_bags(people=guests)
    treat_count = treats(people=guests)
    total_cost = cost(tea_count=tea_count, treat_count=treat_count)
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("tea bags: " + str(tea_count))
    print("treats: " + str(treat_count))
    print("cost: $" + str(total_cost))
    return None


def tea_bags(people: int) -> int:
    """calculate the amount of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """1.5 treat per tea"""
    treats: int = tea_bags(people=people)
    return int(treats * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """finding cost of treats and tea."""
    treat_cost = treat_count * 0.75
    tea_cost = tea_count * 0.50
    return tea_cost + treat_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
