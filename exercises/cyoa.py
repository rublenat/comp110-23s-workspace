"""Exercise 06 - Create your own adventure."""
__author__ = "730396580"

# Emojis.
CONFETTI: str = "\U0001F389"
ARROW: str = "\U000027A1"
SAD: str = "\U0001F62D"
HAPPY: str = "\U0001F917"
WAVE: str = "\U0001F44B"
SHOCK: str = "\U0001F631"
HEAD: str = "\U0001F5E3"
TAIL: str = "\U0001F351"
BOX: str = "\U0001F94A"
MULTI: str = "\U0001F46F"
STAR_EYES: str = "\U0001F929"
TEAR: str = "\U0001F972"

# Globals.
player: str = ""
points: int = 0


def greet() -> None:
    """Welcomes the player."""
    global player 
    player = input("Before we get started, what is your name? ")
    print(f"Hi {player}! Welcome to {HEAD} Heads or Tails {TAIL}")
    print("In this game, you will try and guess coin flip outcomes correctly.")
    print("")
    print(f"{CONFETTI} Here are some rules: {CONFETTI}")
    print(f"{ARROW} 1. You are trying to guess as many correct in a row as possible.")
    print(f"{ARROW} 2. We will keep track of how many you get in a row correct, displayed as 'points'.")
    print(f"{ARROW} 3. 'points' will restart at 0 everytime a coin flip is guessed incorrectly.")


def multiplayer() -> None:
    """Restates the instructions of the game."""
    global player
    global points
    player_two: str = input("What is your name Player2? ")
    player_two_points: int = 0

    print("")
    print(f"Hi {player} and {player_two}! Are you guys ready to compete? {BOX}")
    print("")
    print("Again, here are the rules:")
    print(f"{ARROW} 1. You are trying to guess as many correct in a row as possible.")
    print(f"{ARROW} 2. We will keep track of how many you get in a row correct, displayed as 'points'.")
    print(f"{ARROW} 3. 'points' will restart at 0 everytime a coin flip is guessed incorrectly.")
    print("")
    print("This time, however, you play one at a time.")
    print("The winner will be the one who accumulates the most points.")
    print("")
    
    print(f"{player}, you're up first!")
    points = coin_flip(points)

    print("")
    print(f"Good run {player}. {player_two}, show us what you got!")
    player_two_points = coin_flip(player_two_points)

    if points > player_two_points:
        print(f"You won {player}! {CONFETTI} You get bragging rights with a total of {points} points! {STAR_EYES}")
    if points < player_two_points:
        print(f"You won {player_two}! {CONFETTI} You get bragging rights with a total of {player_two_points} points! {STAR_EYES}")
    if points == player_two_points:
        print(f"Welp! It's a tie. Guess both of you won with {points} points! (or neither of you) {TEAR}")


def coin_flip(points_in_game: int) -> int:
    """Coin flip game function."""
    from random import randint

    guess_word: str = input(f"Do you think it will be {HEAD} heads or {TAIL} tails? ")
    guess_number: int = 0

    if (guess_word == "heads") or (guess_word == "tails"):
        actual: int = randint(1, 2)

        if guess_word == "heads":
            guess_number = 1
        if guess_word == "tails":
            guess_number = 2

        while guess_number == actual and ((guess_word == "heads") or (guess_word == "tails")):
            points_in_game += 1
            guess_word = input("Correct! Guess again: ")

            if guess_word == "heads":
                guess_number = 1
            if guess_word == "tails":
                guess_number = 2
            
            actual = randint(1, 2)

        if guess_number != actual:
            print(f"Oh no! You guessed incorrectly. You ended with {points_in_game} points. {SHOCK}")

    return points_in_game


def main() -> None:
    """Main entrypoint to game."""
    # Initialize globals.
    global points
    global player

    # Welcome the player.
    greet()

    # Choose initial direction.
    print("")
    print("Select an option to continue:")
    print(f"A: Let's Play! {HAPPY}")
    print(f"B: Multiplayer {MULTI}")
    print(f"C: End Game {SAD}")

    next_step: str = input("Choose A, B, or C: ")

    if next_step == "A":
        game: int = coin_flip(points)
        points += game
    if next_step == "B":
        multiplayer()
    if next_step == "C":
        print(f"Bye for now! {WAVE} You ended with {points} points! {SHOCK}")

    # Game loop, choose direction again.
    while (next_step == "A") or (next_step == "B"):
        again: str = input(f"Would you like to play again? Enter 'Yes' {HAPPY} or 'No' {SAD}: ")

        if again == "Yes":
            points = 0
            print("")
            print("Select an option to continue:")
            print(f"A: Let's Play! {HAPPY}")
            print(f"B: Multiplayer {MULTI}")
            next_step = input("Choose A or B: ")

            if next_step == "A":
                game = coin_flip(points)
                points += game
            if next_step == "B":
                multiplayer()

        if again == "No":
            print(f"Bye for now! {WAVE} You ended with {points} points! {SHOCK}")
            next_step = "C"


if __name__ == "__main__":
    main()