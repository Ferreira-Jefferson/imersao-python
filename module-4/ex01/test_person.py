import pytest
from person import Person

def test_person_initialization() -> None:
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30

def test_person_initialization_error() -> None:
    with pytest.raises(TypeError, match="Incorrect name format: receive int expected str"):
        Person(10, "30")  # type: ignore
    
    with pytest.raises(TypeError, match="Incorrect age format: receive str expected int"):
        Person("Alice", "30")  # type: ignore