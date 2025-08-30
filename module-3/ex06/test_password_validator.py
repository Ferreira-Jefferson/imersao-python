import pytest
from password_validator import is_valid_password

values = [
    ("12345678901234567890123456789", False),
    ("A012345678901234", False),
    ("AAAAAaaaaaa11111", False),
    (" 012345678901@aA", False), 
    ("Aa@0123456789012", True),
    ("012345678901@aA", True),
]

@pytest.mark.parametrize("given, expect", values)
def test_password_minus_8(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", values)
def test_password_bigger_16(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", values)
def test_password_has_upper(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", values)
def test_password_has_lower(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", values)
def test_password_has_digit(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", values)
def test_password_has_special_char(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", values)
def test_password_has_space(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect