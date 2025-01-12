"""Example function using unit tests"""

def sum_old(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    idx = 0

    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    
    return sum_total


def sum_old_too(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0

    if len(xs) > 0:
        for item in xs:
            sum_total += item
    
    return sum_total


def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    idx: int = 0

    for idx in range(0, len(xs)):
        item: int = xs[idx]
        sum_total += item
    
    return sum_total