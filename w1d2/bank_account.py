class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance: ", self.balance)
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance: ", self.balance)
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print("Balance: ", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print("Balance: ", self.balance)
            return self


account1 = BankAccount(0.01, 0)
account2 = BankAccount(0.02, 100)

account1.deposit(50).deposit(100).deposit(20).withdraw(160).yield_interest().display_account_info()
account2.deposit(70).deposit(100).withdraw(100).withdraw(100).withdraw(50).withdraw(50).yield_interest().display_account_info()