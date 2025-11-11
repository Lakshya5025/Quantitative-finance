from pathlib import Path
import random
path = Path("quant-week1/day7")
users_file = path / "users.txt"
transactions_file = path / "transactions.txt"
print("Want to login/register:-\n1.Login\n2.Register\n3.Check transactions")
login_register_choice = input("Enter your choice: ")

def accountNumberGenerator():
    account_number = random.randint(1000000000,9999999999)
    return account_number

def newUserTransactionLine():
    with open(users_file, "r", encoding="utf-8") as users:
        lines = users.readlines() 
        line_count = len(lines) + 1
        createEmptyLineInTransactionFile(line_count)
        return line_count
    
def createEmptyLineInTransactionFile(line_number):
    with open(transactions_file, "a", encoding="utf-8") as transactions:
        transactions.write("\n")

def writeInUsersFile(name, password, email, account_number):
    new_user_balance = 0
    new_user_transaction_line = newUserTransactionLine()
    with open(users_file, "a+", encoding="utf-8") as users:
        users.seek(0)
        lines = users.readlines()
        new_user_details = f"account_number:{str(account_number)},name:{name},email:{email},password:{password},balance:0,transaction_line:{new_user_transaction_line}"
        if(len(lines) > 0):users.write("\n")
        users.write(new_user_details)

def validAccountNumber(account_number):
    valid_account = False
    transaction_line = None
    with open(users_file, "r", encoding="utf-8") as users:
            for user in users:
                user_details = user.strip().split(",")
                user_account_number = user_details[0].split(":")[1]
                if(account_number == user_account_number):
                    valid_account = True
                    transaction_line = int(user_details[5].split(":")[1])
                    break
    return {"is_valid":valid_account, "transaction_line":transaction_line} 

def transferMoney(sender_account_number, reciever_account_number, sender_transaction_line, reciever_transaction_line, transfer_amount):
    with open(users_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated = []
    for line in lines:
        raw = line.strip()
        parts = raw.split(",") if raw else []
        if not parts or len(parts) < 6:
            updated.append(line)
            continue

        acc = parts[0].split(":")[1]
        name = parts[1].split(":")[1]
        email = parts[2].split(":")[1]
        password = parts[3].split(":")[1]
        balance = int(parts[4].split(":")[1])
        txn_line = parts[5].split(":")[1]

        if acc == sender_account_number:
            balance = balance - int(transfer_amount)
            line = f"account_number:{acc},name:{name},email:{email},password:{password},balance:{balance},transaction_line:{txn_line}\n"
        elif acc == reciever_account_number:
            balance = balance + int(transfer_amount)
            line = f"account_number:{acc},name:{name},email:{email},password:{password},balance:{balance},transaction_line:{txn_line}\n"

        updated.append(line)

    with open(users_file, "w", encoding="utf-8") as f:
        f.writelines(updated)

    with open(transactions_file, "r", encoding="utf-8") as tf:
        tx_lines = tf.readlines()

    sender_name = ""
    receiver_name = ""
    with open(users_file, "r", encoding="utf-8") as f:
        for u in f:
            parts = u.strip().split(",")
            acc = parts[0].split(":")[1]
            name = parts[1].split(":")[1]
            if acc == sender_account_number:
                sender_name = name
            if acc == reciever_account_number:
                receiver_name = name

    s_idx = int(sender_transaction_line) - 1
    r_idx = int(reciever_transaction_line) - 1

    s_rec = f"{{reciever:{receiver_name}, sender:{sender_name}, amount:{transfer_amount}}}"
    r_rec = f"{{reciever:{receiver_name}, sender:{sender_name}, amount:{transfer_amount}}}"

    s_line = tx_lines[s_idx].rstrip("\n")
    r_line = tx_lines[r_idx].rstrip("\n")

    tx_lines[s_idx] = (s_line + (" ; " if s_line.strip() != "" else "") + s_rec + "\n")
    tx_lines[r_idx] = (r_line + (" ; " if r_line.strip() != "" else "") + r_rec + "\n")

    with open(transactions_file, "w", encoding="utf-8") as tf:
        tf.writelines(tx_lines)
        
def viewTransactionsByAccountNumber(account_number):
    res = validAccountNumber(account_number)
    if not res["is_valid"]:
        print("Invalid account number")
        return

    idx = int(res["transaction_line"]) - 1

    with open(transactions_file, "r", encoding="utf-8") as tf:
        lines = tf.readlines()

    if idx < 0 or idx >= len(lines) or lines[idx].strip() == "":
        print("No transactions found")
        return

    print("Transactions:")
    for part in lines[idx].strip().split(";"):
        p = part.strip()
        if p:
            print(p)
   

def transactionModule(active_user_account_number, active_user_balance, active_user_transaction_line):
    print("Want to transfer money:\n1.Yes\n2.No")
    user_choice = input("What is you choice: ")
    if(user_choice == '1'):
        transfer_acccount = input("Enter account number you want to send money: ")
        response_data = validAccountNumber(transfer_acccount)
        is_valid_transfer_account = response_data['is_valid']
        transfer_account_trasaction_line = response_data['transaction_line']
        if(is_valid_transfer_account):
            transfer_money = int(input("Enter the amount: "))
            if(int(active_user_balance) >= transfer_money):
                transferMoney(sender_account_number=active_user_account_number, reciever_account_number=transfer_acccount, sender_transaction_line=active_user_transaction_line, reciever_transaction_line=transfer_account_trasaction_line, transfer_amount=transfer_money)
            else:
                print("Low balance")
                transactionModule(active_user_account_number=active_user_account_number, active_user_balance=active_user_balance, active_user_transaction_line=active_user_transaction_line)
        else:
            print("Invalid account number")
            transactionModule(active_user_account_number=active_user_account_number, active_user_balance=active_user_balance, active_user_transaction_line=active_user_transaction_line)
        
    elif(user_choice == '2'):
        print("Thank you for you time")
    else:
        print("Please make valid choice")
        transactionModule(active_user_account_number=active_user_account_number, active_user_balance=active_user_balance, active_user_transaction_line=active_user_transaction_line)

if (login_register_choice == '1' ):
    account_number = input("Enter you account number: ")
    password = input("Enter you password: ")
    valid_user = False
    user_account_number = None
    user_name = None 
    user_email = None
    user_balance = None
    user_transaction_line = None
    with open(users_file, "r", encoding="utf-8") as users:
        for user in users:
            user_details = user.strip().split(",")
            user_account_number = user_details[0].split(":")[1]
            user_password = user_details[3].split(":")[1]
            if(account_number == user_account_number and password == user_password):
                valid_user = True
                user_name = user_details[1].split(":")[1]
                user_email = user_details[2].split(":")[1]
                user_balance = user_details[4].split(":")[1]
                user_transaction_line = user_details[5].split(":")[1]
                break
            
    if(valid_user == False):
        print("invalid account number or password")   
    else:
        print(user_account_number)
        print(user_balance)
        print(user_email)
        print(user_transaction_line)
        transactionModule(active_user_account_number=user_account_number, active_user_balance=user_balance, active_user_transaction_line=user_transaction_line)
elif login_register_choice == '2':
    new_user_name = input("Enter you name: ")
    new_user_password = input("Enter you password: ")
    new_user_email = input("Enter you email: ")
    new_user_account_number = accountNumberGenerator()
    writeInUsersFile(name=new_user_name, password=new_user_password, email=new_user_email, account_number=new_user_account_number)
    print("New user created")
    print(f"User name: {new_user_name}")
    print(f"User email: {new_user_email}")
    print(f"User password: {new_user_password}")
    print(f"User account number: {new_user_account_number}")
    
elif login_register_choice == '3':
    acc_no = input("Enter you account number: ")
    viewTransactionsByAccountNumber(account_number=acc_no)
else:
    print("Invalid choice")





"""
user={"account_number":10_digit_number, "name": xyz, "email":abc@gmail.com, "password": someHash, "balance":1234, "transaction_line": line_number_from_transaction_file }

transaction ={reciever:name, sender:name, amount:1234}
"""