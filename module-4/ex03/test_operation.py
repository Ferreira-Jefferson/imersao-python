import pytest
from operation import Operation

def test_operation() -> None:
    result = Operation(1122200, 'ATM deposit')
    assert repr(result) == "Operation(cents=1122200, operation_type='credit', description='ATM deposit')"
    assert str(result) == "R$ 11.222,00 (ATM deposit)"

def test_operation_initialization_error() -> None:
    with pytest.raises(TypeError, match="Incorrect cents format: receive str expected int"):
        Operation("10", 1000)  # type: ignore
    
    with pytest.raises(TypeError, match="Incorrect description format: receive int expected str"):
        Operation(1000, 500)  # type: ignore