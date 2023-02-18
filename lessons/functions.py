""""Practice with Functions"""

print("Hello!")

round(10.25)

# To print ^
print(round(10.25))

# Save function to a value
x: int = round(10.25)
print(x)

# Have to import some functions
from random import randint
z: int = randint(1,7)
print(z)

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same thing"""
    return my_words

xs = mimic("natalie")
print(xs)

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx <= len(my_words):
        return my_words[letter_idx]
    else:
        return "Too high of an index!"

ys = mimic_letter("howdy", 2)
print(ys)

def halve(x: float) -> float:
    print(f"halve({x})")
    return x / 2.0

xxs = halve(4.0)
print(xxs)
