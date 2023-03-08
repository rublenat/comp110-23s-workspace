"""Challenge Question 04 - Dict Function Writing."""


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Creates dictionary with list1 as keys and list2 as corresponding values."""
    dictionary: dict[str, int] = dict()
    idx: int = 0

    if (len(list1) != len(list2)) or (len(list1) == 0) or (len(list2) == 0):
        return dictionary
    
    for idx in range(0, len(list1)):
        dictionary[list1[idx]] = list2[idx]

    return dictionary
