"""Example of defining functions and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: # if number1 < number2
        return number2

x: int = my_max(3, 100)
print(x)

