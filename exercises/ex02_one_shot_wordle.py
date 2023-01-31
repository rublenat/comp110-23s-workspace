"""EX02 - One Shot Wordle."""
__author__ = "730396580"

secret_word: str = "python"
length_of_secret_word: int = len(secret_word)
guess_word: str = input(f"What is your {length_of_secret_word}-letter guess? ")

while len(guess_word) != length_of_secret_word:
    guess_word = input(f"That was not {length_of_secret_word} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx: int = 0
resulting_emoji: str = ""

while idx < length_of_secret_word:
    if guess_word[idx] == secret_word[idx]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        alternate_letter: bool = False
        alternate_idx: int = 0

        while alternate_letter is not True and alternate_idx < length_of_secret_word:
            if secret_word[alternate_idx] == guess_word[idx]:
                alternate_letter = True
            else:
                alternate_idx = alternate_idx + 1
        if alternate_letter is True:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
    idx = idx + 1
print(resulting_emoji)

if guess_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
