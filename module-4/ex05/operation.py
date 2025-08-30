import utils
from enum import Enum

class OperationType(Enum):
    DEBIT = 0
    CREDIT = 1

class Operation:
    cents: int
    operation_type: OperationType
    description: str

    def __init__(self, cents: int, description: str):
        if not cents or not isinstance(cents, int):
            raise TypeError(f"Incorrect cents format: receive {type(cents).__name__} expected int")
        if not description or not isinstance(description, str):
            raise TypeError(f"Incorrect description format: receive {type(description).__name__} expected str")
        self.cents = cents
        self.description = description
        self.operation_type = OperationType.CREDIT if cents > 0 else OperationType.DEBIT
    
    def __repr__(self):
        return f"Operation(cents={self.cents}, operation_type='{self.operation_type.name}', description='{self.description}')"
    
    def __str__(self):
        return f"{utils.format_cents(self.cents)} ({self.description})"
