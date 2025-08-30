import sys

def shrink(value: str) -> str:
    """
    Gets the first 8 characters of a string

    Arguments:
        value(str): complete string

    Returns:
        str: truncated string
    """
    return value[:8]

def enlarge(value: str) -> str:
    """
    Completes a string with 'Z' until it is 8 characters long

    Arguments:
        value(str): original string

    Returns:
        str: 8-character string with 'Z' if it is not 8 characters long
    """
    return value.ljust(8, 'Z')

def main(args: list[str]) -> None:
    """
    Receives arguments passed via the command line and sends them to the functions responsible for
    printing an 8-character string with a 'Z' at the end if it is not the appropriate length.

    Arguments:
        args(list): list of arguments without the file name.

    Returns:
        void: has no return value.
    """
    if len(args) > 0:
        for arg in args:
            print(enlarge(shrink(arg)))
    else:
        print(None)

if __name__ == "__main__":
    main(sys.argv[1:])
