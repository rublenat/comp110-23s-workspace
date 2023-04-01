"""Example function using unit tests"""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs."""
    sum_total: float = 0.0
    idx = 0

    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    
    return sum_total

