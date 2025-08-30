class Person:
    """A simple class to understant the concepts of POO in Python"""
    def __init__(self, name: str, age: int):
        if not name or not isinstance(name, str):
            raise TypeError(f"Incorrect name format: receive {type(name).__name__} expected str")
        if not age or not isinstance(age, int):
            raise TypeError(f"Incorrect age format: receive {type(age).__name__} expected int")
        self.name = name
        self.age = age

    def birthday(self) -> None:
        self.age += 1