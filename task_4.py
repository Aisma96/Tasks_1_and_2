class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Money successfully added to bank account. Current balance: {self.balance}'
        else:
            return 'Can only be positive amount'

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f'Money successfully withdraw from your bank account. Current balance: {self.balance}'
        else:
            return 'You dont have enough money'

    @classmethod
    def from_balance(cls, balance):
        account2 = BankAccount(balance)
        return account2.balance

    @staticmethod
    def from_one_to_another(from_account, to_account, amount):
        if amount <= from_account:
            from_account -= amount
            to_account += amount
            return f'Account1 balance: {from_account}, Account2 balance:{to_account}'
        else:
            return 'Operation is not allowed'


account1 = BankAccount(0)
print(account1.deposit(300))
print(account1.withdraw(50))
print(BankAccount.from_one_to_another(account1.balance, BankAccount.from_balance(0), 200))


