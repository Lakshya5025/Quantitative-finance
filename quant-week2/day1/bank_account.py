class BankAccount:
    def __init__(self, name:str, balance:int):
        self.bal = balance
        self.name = name
    
    def deposite(self, amount:int):
        if(amount > 0):
            self.bal += amount
            print("Deposit success")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount:int):
        if(amount > 0 and amount <= self.bal):
            self.bal -= amount
            print("Withdraw success")
        else:
            print("Invalid amount")
    
    def balance(self):
        print(f"Your current balance is {self.bal}")
        
a_account = BankAccount('a', 500)
a_account.balance()
a_account.withdraw(300)
a_account.balance()
a_account.deposite(400)
a_account.balance()
a_account.withdraw(1000)
a_account.balance()