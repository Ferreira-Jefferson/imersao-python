import sys

def is_positive(value: int) -> bool:
    """
    Verify if the value is positive

    Args:
        value (int): value to verify

    Returns:
        bool: return of verification
    """
    return (value > 0)

if __name__ == '__main__':
    value: int = int(sys.argv[1])
    print(is_positive(value))