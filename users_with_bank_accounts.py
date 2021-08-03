class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account = BankAccount(int_rate=0.019, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f'User: {self.first_name} {self.last_name}, Balance: {self.account.balance}')
        return self
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Interest rate: {self.int_rate}, Balance: {self.balance}')
        return self
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self

brian = User('Brian', 'Gaudet', 'brian@gaudet.com')
biggie = User('Christopher', 'Wallace', 'NotoriousBIG@badboy.com')
daft1 = User('Guy-Manuel', 'de Homem-Christo', 'guy-man@daftpunk.com')

brian.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(50).display_user_balance()

biggie.make_deposit(100000).make_deposit(250000).make_withdrawal(25000).display_user_balance()

daft1.make_deposit(1000000).make_withdrawal(50000).display_user_balance()

brian.transfer_money(daft1, 12).display_user_balance()
daft1.display_user_balance()