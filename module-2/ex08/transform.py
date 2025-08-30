import sys

def square_even_numbers(list_int: list[int]) -> list[int]:
    """
    Receives a string containing numbers separated by spaces, identifies the even numbers,
    and returns a list containing the squares of those numbers.

    Arguments:
        list_int(list[int]): List of integers.

    Returns:
        list[int]: List containing the squares of the even numbers.
    """
    return [number**2 for number in list_int if number % 2 == 0]

def main(args: list[str]) -> None:
    """
    Receives a list of command-line arguments, converts them to a string,
    and prints the squares of the even numbers contained in it.

    Arguments:
        args(list[str]): List of arguments (strings) without the file name.

    Returns:
        None: This function does not return any value; it only prints the result.
    """
    if len(args) == 0:
        return
    list_int: list[int] = []
    for number in args[0].split():
        list_int.append(int(number))
    print("Squared evens:", square_even_numbers(list_int))

if __name__ == "__main__":
    main(sys.argv[1:])