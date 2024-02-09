class Account:
     def __init__(self, owner, balance):
         self.owner = owner
         self.balance = balance
    
     def show_owner(self):
         print(self.owner)
        
     def show_balance(self):
        print(self.balance)
        
     def deposit(self, amount):
         self.balance += amount
        
     def withdraw(self, amount):
         if amount <= self.balance:
             self.balance -= amount
             print("Withdrawal of", amount, "completed.")
         else:
             print("Insufficient funds on the account.")
        
 test = Account("Olzhas", 50000)
 test.show_owner()
 test.show_balance()
 test.deposit(2000)
 test.show_balance()
 test.withdraw(53000)
 test.show_balance()

 

