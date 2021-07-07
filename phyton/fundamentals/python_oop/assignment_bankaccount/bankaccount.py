class BankAccount():
    bank_name = 'Bank of Dojo'

    def __init__(self, accountnumber, int_rate, balance):
        self.accountnumber = accountnumber
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
            if self.balance < 0:
                print("Insufficient Funds")
            else:
                self.balance -= amount
            return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')

    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self


account1 = BankAccount(5050, 0.10, 0)
account2 = BankAccount(6060, 0.15, 0)

account1.deposit(100).deposit(100).deposit(200).withdraw(
    10000).yield_interest().display_account_info()


account2.deposit(1000).deposit(500).withdraw(200).withdraw(100).withdraw(
    100).withdraw(10).yield_interest().display_account_info()

