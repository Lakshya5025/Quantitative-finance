class InsufficientBalanceException(Exception):
    def __init__(self, current_balance):
        self.message = f"Insufficient balancen, your current balance is {current_balance}"
        super().__init__(self.message)

class ATM:
    def __init__(self, amount):
        self.amount = amount
        
    def withdraw(self, amount):
                    
        if(self.amount >= amount):
            self.amount -= amount
            print("Successfully withdraw")
            print(f"Account balance : {self.amount}")
        else:
            raise InsufficientBalanceException(self.amount)
        

user = ATM(500)
try:
    user.withdraw(5800)
except InsufficientBalanceException as e:
    print(e)

        