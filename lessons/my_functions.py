"""importing functions"""

def addition(int1: int, int2: int) -> int:
    return int1 + int2

my_variable: str = "hello"

if __name__ == "main":
    print("this should only run when running my functions")
else:
    print("my functions is being imported")