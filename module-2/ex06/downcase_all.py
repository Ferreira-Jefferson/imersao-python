import sys

def downcase_it(value: str) -> str:
    """
    Convert string to lowercase

    Args:
        value (str): string in anycase

    Returns:
        str: string parsed to lowercase
    """
    return value.lower()

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print(None)
    else:
        for value in sys.argv[1:]:
            print(downcase_it(value))
    