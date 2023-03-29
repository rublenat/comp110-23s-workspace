"""Lesson 12 - Lists"""

grocery_list: list[str] = ["bananas", "milk"]

grocery_list = grocery_list.append("bread")

from random import randint

actual = 0

name = randint(1, 2)

print(name)

def odd_and_even(list: list[int]) -> list[int]:
    new_list: list[int] = []
    i: int = 0

    while i < len(list):
        if i % 2 == 0:
            new_list.append(list[i])
        i += 1
    
    i = 0
    while i < len(new_list):
        if new_list[i] % 2 == 0:
            new_list.pop(i)
        i += 1

    return new_list

def value_exists(input, x) -> bool:
    for item in input:
        if input[item] == x:
            return True
    
    return False

def short_words(input: list[str]) -> list[str]:
    new_list: list[str] = []

    for item in input:
        if len(item) < 5:
            new_list.append(item)
        else:
            print(f"{item} was more than 5 characters.")

    return new_list

my_list = ['bike', 'scooter', 'unicycle']

for x in my_list:
    print(x)

def shrink(input: dict[str, int]) -> list[int]:
    new_list: list[int] = []

    for y in input:
        if input[y] % 2 == 0 and input[y] < 11:
            new_list.append(input[y])
    
    return new_list

my_dict = {'strawberry': 8, 'vanilla': 10, 'mint': 12}
new = shrink(my_dict)
print(new)

d = {'lab': 4, "bulldog": 5, "pom": 10}
print(len(d))

