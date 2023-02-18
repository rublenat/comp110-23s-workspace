"""EX03 - Structured Wordle."""
__author__ = "730396580"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Searches for given character in given word."""
    assert len(character) == 1
    idx: int = 0
    in_word: bool = False

    while idx < len(word):
        if word[idx] == character:
            in_word = True

        idx = idx + 1
    return in_word


def emojified(guess: str, secret_word: str) -> str:
    """Returns emoji boxes based on whether characters in guess and secret word match."""
    assert len(guess) == len(secret_word)
    idx: int = 0
    emoji: str = ""

    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret_word, guess[idx]) is True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Given expected length will ask user for guess word of that same length."""
    word_given: str = input(f"Enter a {expected_length} character word: ")

    while len(word_given) != expected_length:
        word_given = input(f"That wasn't {expected_length} chars! Try Again: ") 
    return word_given


def main() -> None:
    """The entry point of the program and the main game loop."""
    secret: str = "codes"
    turns: int = 1
    guess_word: str = ""

    while (turns < len(secret)) and (guess_word != secret):
        print(f"=== Turn {turns}/6 ===")
        guess_word = input_guess(len(secret))
        print(emojified(guess_word, secret))

        if guess_word != secret:
            turns = turns + 1

    if guess_word == secret:
        print(f"You won in {turns}/6 guesses!")
    if guess_word != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()