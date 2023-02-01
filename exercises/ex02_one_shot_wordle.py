"""EX02 - One Shot Wordle."""
__author__ = "730396580"

# Asking user for their guess on the secret word 
secret_word: str = "python"
length_of_secret_word: int = len(secret_word)
guess_word: str = input(f"What is your {length_of_secret_word}-letter guess? ")

# If the user's guess does not match the number of letters, gives an error and asks for input of another guess
while len(guess_word) != length_of_secret_word:
    guess_word = input(f"That was not {length_of_secret_word} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx: int = 0
resulting_emoji: str = ""

# Checking to see if each index of secret word and guess word match, gives different color box based on outcome
# Only repeating the loop while the index value is less than the length of the secret word
# Index goes up by one after each loop in order for the whole word to be searched

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

# If the guess word is the secret word tells the user they were right, if the guess was wrong tells them to guess again
if guess_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
