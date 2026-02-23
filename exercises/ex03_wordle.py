"""ex03 Wordle"""

__author__ = "730941956"


def input_guess(secret_word_len: int) -> str:
    """prompts the user for a guess of the correct length"""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # asking user to input a ward for guess var.

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """returns True if char_guess is found in secret_word, otherwise False"""
    assert len(char_guess) == 1

    index: int = 0  # initializing index to start scanning the secret_word
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
    index += 1  # repeat loop until false.

    return False


def emojified(guess: str, secret: str) -> str:
    """returns a string of emojis evaluating the guess."""
    assert len(guess) == len(
        secret
    )  # ensures both strings are the same length before comparing.

    white_box: str = "\U00002b1c"  # unicode emoji str
    green_box: str = "\U0001f7e9"
    yellow_box: str = "\U0001f7e8"

    index: int = 0  # sets index to 0 and initializes an empty string emoji_results
    emoji_results: str = ""

    while index < len(guess):
        if guess[index] == secret[index]:  # matching characters
            emoji_results += green_box
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            emoji_results += yellow_box
        else:
            emoji_results += white_box
        index += (
            1  # causes the while loop to start over, looking at next letter via index.
        )

    return emoji_results


def main(secret: str) -> None:  # main fn controls game state
    """the entrypoint of program and main game loop"""
    current_turn: int = 1  # initializing
    max_turns: int = 6  # initializing
    won: bool = False  # initializing

    # the game loop will run as long as user has turns left and hasn't won yet
    while current_turn <= max_turns and not won:
        print("f== Turn {current_turn}/{max_turns} ===")

        # ask for guess using the helper function
        user_guess: str = input_guess(
            secret_word_len=len(secret)
        )  # calls input_guess & stores result in user_guess
        # print the emojis using the helper function
        print(
            emojified(guess=user_guess, secret=secret)
        )  # call emojified using the guess & secret word, prints result.
        # check for the win condition
        if user_guess == secret:
            won = True
        else:
            current_turn += 1

    # after loop is done, check why it finished
    if won:
        print(f"you won in {current_turn}/{max_turns} turns!")  # winning output
    else:
        print(f"X/{max_turns} - sorry, try again tomorrow!")  # losing ouput

    if __name__ == "__main__":
        main(secret="codes")
