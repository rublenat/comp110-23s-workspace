"""EX07 - Dictionary Functions."""
__author__ = "730396580"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    list_one: list[str] = []
    list_two: list[str] = []
    new_dict: dict[str, str] = {}
    idx: int = 0
    idx2: int = 1

    for key in input:
        list_one.append(input[key])
        list_two.append(key)

    while idx2 < len(list_one):
        if list_one[idx] == list_one[idx2]:
            raise KeyError("Dictionaries cannot have multiple of the same key (check to see if values of original dictionary are the same)!")
        idx2 += 1
        idx += 1
    
    idx = 0
    while idx < len(list_one):
        new_key: str = list_one[idx]
        new_value: str = list_two[idx]
        new_dict[new_key] = new_value
        idx += 1
    
    return new_dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns color that appears the most frequently."""
    new_dict: dict[str, int] = {}
    colors: list[str] = []
    number_per_color: list[int] = []
    idx: int = 0
    max: str = ''

    for key in input:
        colors.append(input[key])
    
    while idx < len(colors):
        specific_color: str = colors[idx]
        idx2: int = 0
        count: int = 0
        while idx2 < len(colors):
            if colors[idx2] == specific_color:
                count += 1
            idx2 += 1
        number_per_color.append(count)
        idx += 1
    
    idx = 0
    while idx < len(colors):
        new_key: str = colors[idx]
        new_value: int = number_per_color[idx]
        new_dict[new_key] = new_value
        idx += 1
    
    if len(colors) >= 1:
        max = colors[0]
        for key in new_dict:
            for keys in new_dict:
                if new_dict[key] < new_dict[keys]:
                    max = keys

    return max


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of times each value appears in input list."""
    new_dict: dict[str, int] = {}
    idx: int = 0

    while idx < len(input):
        if input[idx] in new_dict:
            new_dict[input[idx]] += 1
        else:
            new_dict[input[idx]] = 1
        idx += 1

    return new_dict