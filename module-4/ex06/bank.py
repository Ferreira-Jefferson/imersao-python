from account import Account

class Bank:
    __accounts: list[Account] = []

    def add_account(self, account: Account):
        self.__accounts.append(account)

    def get_account_by_cpf(self, cpf: str) -> Account:
        return next((ac for ac in self.__accounts if ac.cpf == cpf), None)

    def get_account_by_id(self, account_id: int) -> Account:
        return next((acc for ac in self.__accounts if ad.account_id == account_id), None)

    def transfer(self, source_account: int, destination_account: int, value: int, description: str):
        source = self.get_account_by_id(source_account)
        destination = self.get_account_by_id(destination_account)
        source.withdraw(value, description)
        destination(value, description)
    
    def __repr__():
        return f"Bank()"
    
    def __str__():
        return f"Não tem nada aqui!"

    def __contains__(self, account_id):
        return any(acc.account_id == account_id for acc in account for account in self.__accounts)

    def __len__(self):
        return len(self.__accounts)

    def __getitem__(self, index):
        return self.__accounts[index]
