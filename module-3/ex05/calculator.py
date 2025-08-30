from typing import Any

def power(base: int, exponent: int) -> Any:
    """Returns the result of raising base to the given exponent."""
    return base ** exponent

def add(value_1: int, value_2: int) -> int:
    """Returns the sum of two integers."""
    return value_1 + value_2

def subtract(value_1: int, value_2: int) -> int:
    """Returns the difference between two integers."""
    return value_1 - value_2

def multiply(value_1: int, value_2: int) -> int:
    """Returns the product of two integers."""
    return value_1 * value_2

def divide(value_1: int, value_2: int) -> float:
    """Returns the result of dividing two integers, raises error if divisor is zero."""
    if value_2 == 0:
        raise ValueError('Cannot divide by zero')
    return value_1 / value_2
