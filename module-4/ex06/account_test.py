import pytest
from account import Account, InsufficientBalance
from operation import Operation
import utils

def test_account_creation_valid():
    acc = Account(123, "12345678900")
    assert acc.account_id == 123
    assert acc.cpf == "12345678900"
    assert repr(acc) == "Account(123, '12345678900')"

def test_account_creation_invalid_id():
    with pytest.raises(TypeError):
        Account("abc", "12345678900")

def test_account_creation_invalid_cpf():
    with pytest.raises(TypeError):
        Account(123, 99999999999)

def test_deposit_valid():
    acc = Account(1, "11111111111")
    acc.deposit(10000, "Depósito inicial")
    assert str(acc).startswith("Account: 1")
    assert "R$ 100,00" in str(acc)

def test_deposit_invalid_zero():
    acc = Account(1, "11111111111")
    with pytest.raises(ValueError):
        acc.deposit(0, "Valor inválido")

def test_deposit_invalid_negative():
    acc = Account(1, "11111111111")
    with pytest.raises(ValueError):
        acc.deposit(-500, "Valor negativo")

def test_withdraw_valid():
    acc = Account(1, "11111111111")
    acc.deposit(10000, "Depósito")
    acc.withdraw(5000, "Saque")
    assert "R$ 50,00" in str(acc)

def test_withdraw_invalid_zero():
    acc = Account(1, "11111111111")
    with pytest.raises(ValueError):
        acc.withdraw(0, "Valor inválido")

def test_withdraw_invalid_negative():
    acc = Account(1, "11111111111")
    with pytest.raises(ValueError):
        acc.withdraw(-100, "Valor negativo")

def test_withdraw_insufficient_balance():
    acc = Account(1, "11111111111")
    acc.deposit(1000, "Depósito")
    with pytest.raises(InsufficientBalance):
        acc.withdraw(2000, "Saque excessivo")

def test_operations_recorded_correctly():
    acc = Account(1, "11111111111")
    acc.deposit(5000, "Depósito")
    acc.withdraw(2000, "Saque")
    # Acessando via name mangling
    ops = acc._Account__operations
    assert len(ops) == 2
    assert ops[0].cents == 5000
    assert ops[1].cents == -2000
