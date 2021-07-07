class User():
    bank_name = "First National Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: ${self.account_balance}')


guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
bruno = User('Bruno Marek', 'brunomarek@python.com')

guido.make_deposit(100).make_deposit(200).make_deposit(500)
monty.make_deposit(50).make_deposit(500)
bruno.make_deposit(1000)


guido.make_withdrawal(100)
monty.make_withdrawal(30).make_withdrawal(100)
bruno.make_withdrawal(200).make_withdrawal(300).make_withdrawal(100)

print(guido.account_balance)
print(monty.account_balance)
print(bruno.account_balance)
guido.display_user_balance()
monty.display_user_balance()
bruno.display_user_balance()