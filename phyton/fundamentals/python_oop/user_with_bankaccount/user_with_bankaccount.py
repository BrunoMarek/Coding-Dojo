class BankAccount():
    bank_name = 'Bank of Dojo'

    def __init__(self, int_rate, balance):
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


account1 = BankAccount(0.10, 0)
account2 = BankAccount(0.15, 0)
contadalala = BankAccount(100, 0)

# contadalala.deposit(1000).deposit(50000).withdraw(10000).yield_interest().display_account_info()
# account1.deposit(100).deposit(100).deposit(200).withdraw(
#     10000).yield_interest().display_account_info()


# account2.deposit(1000).deposit(500).withdraw(200).withdraw(100).withdraw(
#     100).withdraw(10).yield_interest().display_account_info()


class User():
    bank_name = "Bank of Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    
    def make_deposit(self, amount):
        self.account.deposit(100)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw
        return self
    
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: ${self.account.display_account_info()}')


guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
bruno = User('Bruno Marek', 'brunomarek@python.com')

guido.make_deposit(100).make_deposit(200).make_deposit(500)
monty.make_deposit(50).make_deposit(500)
bruno.make_deposit(1000)


guido.make_withdrawal(100)
monty.make_withdrawal(30).make_withdrawal(100)
bruno.make_withdrawal(200).make_withdrawal(300).make_withdrawal(100)


guido.display_user_balance()
monty.display_user_balance()
bruno.display_user_balance()