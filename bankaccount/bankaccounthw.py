class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.deposit += amount
        return self

    def withdraw(self, amount):
      if (self.balance - amount) >=0:
        self.withdraw -= amount
      else:
        print ("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
        return self

    def display_account_info(self):
        self.display_account_info('Balance')
        return self

    def yield_interest(self):
        if self. balance >0:
          self.balance += (self.balance * self.int_rate)
          return self

class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate=0.2, balance=0)

    def deposit(self, amount):
      self.account.deposit(amount) 
      return self

    def withdraw(self, amount):
      self.account.withdraw(amount)
      return self

    def display_account_balance (self):
      self.account.display_account_info()
      return self
    

jim = User('Jim Wells', 'gohard@home.com')
jim.deposit(900).withdraw(400) 
print(jim.account.balance) 

