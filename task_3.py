class BankAccount:
    total_account = 0

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        BankAccount.total_account += 1

    def show_balance(self):
        return f'{self.owner} current balance: {self.balance}'

    @classmethod
    def get_total_accounts(cls):
        return f'Total bank account: {cls.total_account}'

    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False


bank_account1 = BankAccount('Mark', 2563.25)
bank_account2 = BankAccount('Josh', 584.2)
bank_account3 = BankAccount('Mike', 10000)

print(bank_account1.show_balance())
print(bank_account2.show_balance())
print(bank_account3.show_balance())

print(BankAccount.get_total_accounts())

print(BankAccount.validate_amount(100))
print(BankAccount.validate_amount(-20))
