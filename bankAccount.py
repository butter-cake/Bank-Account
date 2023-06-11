class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("insufficient funds: Charging a $5 fee")
            self.balance = self.balance  - 5
            return self
        self.balance = self.balance  - amount
        return self

    def display_account_info(self):
        print("Balance: ", self.balance)

    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance*self.int_rate
            return self
        return self
b1 = BankAccount(1.05, 5000).deposit(1500).deposit(250).deposit(3000).withdraw(2500).yield_interest().display_account_info()
b2 = BankAccount(1.08, 2500).deposit(2000).deposit(1000).withdraw(1000).withdraw(500).withdraw(1250).withdraw(100).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(1.05, 2500)
    
    def make_desposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self