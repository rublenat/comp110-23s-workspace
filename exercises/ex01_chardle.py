"""EX01 - Chardle - A cute step towards Wordle."""
__author__ = "730396580"

enter_a_word = str = input("Enter a 5-character word: ")
if (len(enter_a_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
enter_a_single_letter = str = input("Enter a single character: ")
if (len(enter_a_single_letter) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + enter_a_single_letter + " in " + enter_a_word)

if (enter_a_single_letter == enter_a_word[0]):
    print(enter_a_single_letter + " found at index 0")

if (enter_a_single_letter == enter_a_word[1]):
    print(enter_a_single_letter + " found at index 1")
    
if (enter_a_single_letter == enter_a_word[2]):
    print(enter_a_single_letter + " found at index 2")

if (enter_a_single_letter == enter_a_word[3]):
    print(enter_a_single_letter + " found at index 3")

if (enter_a_single_letter == enter_a_word[4]):
    print(enter_a_single_letter + " found at index 4")

instances_count = 0

if enter_a_single_letter == enter_a_word[0]:
    instances_count = instances_count + 1
if enter_a_single_letter == enter_a_word[1]:
    instances_count = instances_count + 1
if enter_a_single_letter == enter_a_word[2]:
    instances_count = instances_count + 1
if enter_a_single_letter == enter_a_word[3]:
    instances_count = instances_count + 1
if enter_a_single_letter == enter_a_word[4]:
    instances_count = instances_count + 1

if (instances_count == 1):
    print(instances_count, "instance of " + enter_a_single_letter + " found in " + enter_a_word)
if (instances_count > 1):
    print(instances_count, "instances of " + enter_a_single_letter + " found in " + enter_a_word)
if (instances_count == 0):
    print("No instances of " + enter_a_single_letter + " found in " + enter_a_word)