from operation import Operation, OperationType
import utils

class InsufficientBalance(Exception):
    def __init__(self, message):
        super().__init__(message)

class Account:
    account_id: int
    cpf: str
    __balance: float
    __operations: list[Operation]

    def __init__(self, account_id: int, cpf: str):
        if not account_id or not isinstance(account_id, int):
            raise TypeError(f"Incorrect account_id format: receive {type(account_id).__name__} expected int")
        if not cpf or not isinstance(cpf, str):
            raise TypeError(f"Incorrect cpf format: receive {type(cpf).__name__} expected str")
        self.account_id = account_id
        self.cpf = cpf
        self.__balance = 0
        self.__operations = []
    
    def deposit(self, amount: int, description: str) -> None:
        if amount <= 0:
            raise ValueError('valor deve ser > 0')
        op = Operation(amount, description)
        self.__operations.append(op)
        self.__balance += amount


    def withdraw(self, amount: int, description: str) -> None:
        if amount <= 0:
            raise ValueError('valor deve ser > 0')
        if amount > self.__balance:
            raise InsufficientBalance('saldo insuficiente')
        op = Operation(amount * -1, description)
        self.__operations.append(op)
        self.__balance -= amount

    def statement(self) -> None:
        for op in self.__operations:
            print(f"{'[+]' if  op.operation_type.name == 'CREDIT' else '[-]'} {utils.format_cents(op.cents)} ({op.description})")
            print(f"Balance: {'[+]' if op.operation_type.name == 'CREDIT' else '[-]'} {utils.format_cents(op.cents)}")
    
    def __repr__(self):
        return f"Account({self.account_id}, '{self.cpf}')"
    
    def __str__(self):
        return f"Account: {self.account_id}\nBalance: {'[+]' if self.__balance >= 0 else '[-]'} {utils.format_cents(self.__balance)}"