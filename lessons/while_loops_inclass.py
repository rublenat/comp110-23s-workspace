"""Asks user for number, goes until it is correct"""

SECRET: int = 4
guess_number: int = int(input("Guess a number: "))
playing: bool = True

while playing:
    if guess_number == SECRET:
        print("Yay! Yu got it right!")
        playing = False
    else:
        print("Wrong number")
        if guess_number % 2 != 0: # Guess is odd number
            print("Your guess is odd, the answer is even.")
        if guess_number > SECRET:
            print("your guess is too high")
        else:
            print("guess is too low")
        guess_number = int(input("Guess another number:"))
