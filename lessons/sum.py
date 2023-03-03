"""Example function using unit tests"""

def sum_old(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    idx = 0

    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    
    return sum_total


def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    idx: int = 0
    item: int = xs[idx]

    for item in xs:
        sum_total += item
    
    return sum_total
