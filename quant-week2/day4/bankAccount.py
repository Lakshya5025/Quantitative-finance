import json
from datetime import datetime
import os
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = float(balance)
        self.created_at = datetime.now().isoformat()
        self.transactions = []

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.transactions.append({
            "type": "deposit",
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transactions.append({
            "type": "withdraw",
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })

    def to_dict(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "created_at": self.created_at,
            "transactions": self.transactions
        }


def save_account(account, path):
    with open(path, "w") as f:
        json.dump(account.to_dict(),f, indent=2)


def load_account(path):
    with open(path, "r") as f:
        data = json.load(f)

    acc = BankAccount(data["owner"], data["balance"])
    acc.created_at = data["created_at"]
    acc.transactions = data["transactions"]
    return acc



base = os.getcwd()
data_dir = os.path.join(base, "quant-week2\\day4")
file_path = os.path.join(data_dir, "data.json")
print(file_path)
a = BankAccount("Lakshya", 1000)
a.deposit(250.5)
a.withdraw(100.75)

print("Before saving:", a.to_dict())
save_account(a, file_path)

loaded = load_account(file_path)
print("Loaded:", loaded.to_dict())
