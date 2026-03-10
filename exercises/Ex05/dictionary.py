"""Dictionary Utility Functions."""

__author__ = "730941956"  # step 0


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Step 1."""
    result: dict[str, str] = {}

    for key in input_dict:
        value = input_dict[key]

        if value in result:
            raise KeyError("Duplicate value found!")

        result[value] = key

    return result


def favorite_color(names_colors: dict[str, str]) -> str:
    """Step 2."""
    color_counts: dict[str, int] = {}

    for name in names_colors:
        color = names_colors[name]

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_popular = ""
    highest_count = 0

    for color in color_counts:
        if color_counts[color] > highest_count:
            most_popular = color
            highest_count = color_counts[color]

    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Step 3."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Step 4."""
    result: dict[str, list[str]] = {}

    for word in words:
        if word.isalpha():
            letter = word[0].lower()

            if letter in result:
                result[letter].append(word)
            else:
                result[letter] = [word]

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Step 5."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
