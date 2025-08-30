import pytest
from utils import format_cents

values = [
    (0, 'R$ 0,00'),
    (10, 'R$ 0,10'),
    (100, 'R$ 1,00'),
    (100_42, 'R$ 100,42'),
    (1_000_42, 'R$ 1.000,42'),   
    (11_222_00, 'R$ 11.222,00'),
    (42_42_42_42_0, 'R$ 4.242.424,20'),
]

@pytest.mark.parametrize("given, expected", values)
def test_format_cents(given: int, expected: str) -> None:
    assert format_cents(given) == expected
