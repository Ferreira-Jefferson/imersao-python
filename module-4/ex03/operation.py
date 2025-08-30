import utils

class Operation:
    cents: int
    operation_type: str
    description: str

    def __init__(self, cents: int, description: str):
        if not cents or not isinstance(cents, int):
            raise TypeError(f"Incorrect cents format: receive {type(cents).__name__} expected int")
        if not description or not isinstance(description, str):
            raise TypeError(f"Incorrect description format: receive {type(description).__name__} expected str")
        self.cents = cents
        self.description = description
        self.operation_type = 'credit' if cents > 0 else 'debit'
    
    def __repr__(self):
        return f"Operation(cents={self.cents}, operation_type='{'credit' if self.cents > 0 else 'debit'}', description='{self.description}')"
    
    def __str__(self):
        return f"{utils.format_cents(self.cents)} ({self.description})"
