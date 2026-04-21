"""exploring lists and while loops through a party rsvp example."""

# Global list: friends who has RSVPed that they are going to the party
rsvp_list: list[str] = ["Enrico", "yun"]


def add_rsvp(rsvped: list[str], friend: str) -> None:
    """Mutate the list by appending a friend."""
    rsvped.append(friend)


print(rsvp_list)
add_rsvp(rsvped=rsvp_list, friend="Alex")
print(rsvp_list)


def has_rsvped(rsvped: list[str], friend: str) -> bool:
    """check that a friend has RSVPed to the party by adding them to the list."""
    idx: int = (
        0  # could name i or idx to represent current index were looking at in list.
    )
    while idx < len(rsvped):
        if rsvped[idx] == friend:
            return True
        idx += 1
        return False
    # never equal to or greater than bc it messes up loop. wnt to visit multiple values.


def not_yet_rsvped(rsvped: list[str], invited: list[str]) -> list[str]:
    """Return list of names of people who have yet to RSVP"""
