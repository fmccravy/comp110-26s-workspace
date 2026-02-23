"""EX02 Chardle - My own version of Wordle."""

__author__ = "730941956"


def input_word() -> (
    str
):  # parameters are supposed to be empty - there is not an actual secret word in this assignment - any word the user inputs will run this code.
    """Prompts the user to type a 5 letter word."""
    word = input()
        "Enter a 5-character word: "
    )  # Word will be defined later. Input is a function call that is built in, not one I define.
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # this exit() stops the function after it prints the error, but before it returns anything!
    return word


def input_letter() -> str:  # parameters are supposed to be empty!
    """Prompts the user to type 1 letter."""
    letter = input("Enter a single character: ")
    if (
        len(letter) != 1
    ):  # Need to remember that len gives amount of number, indexing is not needed yet.
        print("Error: Character must be a single character.")
        exit()  # same as line 11
    return letter


def contains_char(word: str, letter: str) -> None:
    """checking where character appears in a word."""
    print(
        f"Searching for {letter} in {word}"
    )  # This does not give user the secret word, it shows their guess.
    count = 0  # <- needed to define count near top of function for it to run!
    if word[0] == letter:
        print(
            f"{letter} found at index 0"
        )  # this line states that 'letter is found at index 0', this is not because I know what user will type, this is a conditional. Line only runs if the users input makes it true. If not true, python skips this and does not print.
        count = count + 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count = count + 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count = count + 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count = count + 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count = count + 1
    if (
        count == 0
    ):  # The next few lines use if, elif, and else since count cannot give an output showing either 0 or more than 1 instances of a letter being found in the word.
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:  # this is the main function, maybe it could go at the top - unsure.
    """Entry point of Chardle Game!"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
