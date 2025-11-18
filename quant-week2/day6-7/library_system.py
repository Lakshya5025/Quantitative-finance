import os, json
import random
curr_dir = os.getcwd()
data_folder_path = os.path.join(curr_dir, "quant-week2\\day6-7\\data")
books_records = os.path.join(data_folder_path, "books.json")
members_records = os.path.join(data_folder_path, "members.json")

class InvalidAgeException(Exception):
    def __init__(self, *args):
        self.message = "Age must be in range of 7 to 100"
        super().__init__(*args)
class InvalidBalanceException(Exception):
    def __init__(self, *args):
        self.message = "Balance must be positive number"
        super().__init__(*args)
class InsuffecientBalanceException(Exception):
    def __init__(self, *args):
        self.message = "Insuffecient balance"
        super().__init__(*args)
class InvalidCopies(Exception):
    def __init__(self, *args):
        self.message = "Number of copies must be positive"
        super().__init__(*args)

    
class Member():
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance - 50
        self.membership_number = memberNumberGenerator()
    def save_member(self):
        if(self.age >= 7 and self.age <= 100):
            if(self.balance >= 0):
                with open(members_records, "r", encoding='utf-8') as f:
                    members = json.load(f)
                    members.append(createJSONOfMember(self))
                with open(members_records, "w", encoding='utf-8') as f:
                    json.dump(members, f, indent=2)
            else:
                raise InvalidBalanceException()
        else:
            raise InvalidAgeException()
            
class Book():
    def __init__(self, title, author, price, rent_price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.rent_price = rent_price
        self.copies = copies
    
    def save_books_details(self):
        if(self.copies > 0):
            with open(books_records, "r", encoding='utf-8') as f:
                available_books_list = json.load(f)
                total_books = len(available_books_list)
                available_books_list.append(createJSONOfBook(self,total_books))
            with open(books_records, "w", encoding="utf-8") as f:
                json.dump(available_books_list, f, indent=2)
        else:
            raise InvalidCopies()
                


def memberNumberGenerator():
    member_number = random.randint(1000000000,9999999999)
    return member_number 
            
def createJSONOfBook(book, book_id):
    return {
    "id": book_id + 1 ,
    "title": book.title,
    "author": book.author,
    "rent_price": book.rent_price,
    "price": book.price,
    "copies": book.copies,
    "left_copies": book.copies
  }
    
def createJSONOfMember(member):
    return {
        "membership_number" : member.membership_number,
        "name" : member.name,
        "age" : member.age,
        "balance" : member.balance,
        "rented_books" : [],
        "bought_books" : []
    }
    
def createTransactionJSON(book, type):
    amount = 0
    if(type == "rent"):
        amount = book['rent_price']
    elif(type == "purchase"):
        amount = book['price']
    
    return {
        "book_id":book['id'],
        "book" : book['title'],
        "type" : type,
        "amount" : amount,        
    }

def getAllBooks():
    with open(books_records, "r", encoding='utf-8') as f:
        available_books_list = json.load(f)
        for book_details in available_books_list:
            if(book_details['left_copies'] > 0):
                print(f"Id:{book_details['id']}, {book_details['title']}, {book_details['author']}, Price:{book_details['price']}, Rent:{book_details['rent_price']}")

def memberExists(membership_number):
    flag = False
    with open(members_records, "r", encoding='utf-8') as f:
        members = json.load(f)  
        for member in members: 
            if(member['membership_number'] == membership_number):
                flag = True
                break
    return flag
  
def isBookAvailable(id):
    flag = False
    with open(books_records, 'r', encoding='utf-8') as f:
        books = json.load(f)
        for book in books:
            if(book['id'] == id):
                if(book['left_copies'] > 0):
                    flag = True
                    break
                else:
                    print("Out of stock")
                    break
    return flag

def isBookExists(id):
    flag = False
    with open(books_records, 'r', encoding='utf-8') as f:
        books = json.load(f)
        for book in books:
            if(book['id'] == id):
                flag = True
                break
    print("Book exist function")
    return flag


def doesMemberHasBook(id, membership_number):
    with open(members_records, "r", encoding='utf-8') as f:
        members = json.load(f)
        for member in members:
            if(member['membership_number'] == membership_number):
                rented_books = member['rented_books']
                for rented_book in rented_books:
                    if(rented_book['book_id'] == id): return True
                return False
    print("member has book function")


def returnRentedBook(membership_number, book_id):
    if(memberExists(membership_number=membership_number) and isBookExists(id=book_id) and doesMemberHasBook(book_id, membership_number)):
        print("working fine 0")
        with open(books_records, "r", encoding='utf-8') as f:
            books = json.load(f)
            for book in books:
                if(book["id"] == book_id):
                    book["left_copies"] += 1
        print("Working Fine 1")
        with open(books_records, "w", encoding="utf-8") as f:
            json.dump(books, f, indent=2)
        print("Working Fine 2")

        with open(members_records, "r", encoding="utf-8") as f:
            members = json.load(f)
            for member in members:
                if(member['membership_number'] == membership_number):
                    rented_books = member['rented_books']
                    updated_rented_books = []
                    for rented_book in rented_books:
                        if(rented_book['book_id'] != book_id):
                            updated_rented_books.append(rented_book)
                    member['rented_books'].clear()
                    for rented_book in updated_rented_books:
                        member['rented_books'].append(rented_book)
        print("Working Fine 3")
        with open(members_records, "w", encoding="utf-8") as f:
            json.dump(members, f, indent=2)
        print("Successfully returned")       
        print("Working Fine 4")

    elif(not doesMemberHasBook(id=book_id, membership_number=membership_number)):
        print("Member don't have this book")
    elif(not memberExists(membership_number=membership_number)):
        print("Member not registered")
    else:
        print("Book out of stock")

def updateTransactionInMembersFile(membership_number, book, type):
    with open(members_records, "r", encoding="utf-8") as f:
        members = json.load(f)
        for member in members:
            if(member['membership_number'] == membership_number):
                if(type == 'rent'):
                    member['balance'] -= book["rent_price"]
                    member["rented_books"].append(createTransactionJSON(book=book, type=type))
                elif(type == 'purchase'):
                    member['balance'] -= book["price"]
                    member["bought_books"].append(createTransactionJSON(book=book, type=type))
    with open(members_records, "w", encoding='utf-8') as f:
        json.dump(members, f, indent=2)
                    
def rentOrPurchase(id, membership_number, type):
    if(memberExists(membership_number=membership_number) and isBookAvailable(id=id)):
        rented_or_bought_book = {}
        with open(books_records, "r", encoding='utf-8') as f:
            books = json.load(f)
            for book in books:
                if(book['id'] == id):
                    rented_or_bought_book = book
                    if(type == "purchase"):
                        book['copies'] -= 1
                    book['left_copies'] -= 1
        with open(books_records, 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=2)
        updateTransactionInMembersFile(membership_number=membership_number,book=rented_or_bought_book,type=type )
        print("Transaction Successfull")
    elif(not memberExists(membership_number)):
        print("Member not registered")
    else :
        print("Book out of stock")

print("Operations you can perform:-\n1.Add new book\n2.Add new member(Registration fee - 50)\n3.Available Books\n4.Rent book\n5.Purchase book\n6.Return book")
user_choice = input("Enter you choice: ")
if(user_choice  == '1'):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    price = int(input("Enter book price: "))
    rent_price = int(input("Enter book rent price: "))
    copies = int(input('Enter number of copies: '))
    new_book = Book(title=title, author=author, price=price, rent_price=rent_price, copies=copies)
    try:
        new_book.save_books_details()
    except InvalidCopies as e:
        print(e.message)
elif(user_choice == '2'):
    name = input("Enter member name: ")
    age = int(input("Enter member age: "))
    balance = int(input("Enter user balance: "))
    new_member = Member(name=name, age=age, balance=balance)
    try:
        new_member.save_member()
    except InvalidAgeException as e:
        print(e.message)
    except InvalidBalanceException as e:
        print(e.message)

elif(user_choice == '3'):
    getAllBooks()
elif(user_choice == '4'):
    book_id = int(input("Enter book id: "))
    membership_number = int(input("Enter you membership number: "))
    rentOrPurchase(id=book_id, membership_number=membership_number, type="rent")
    
elif(user_choice == '5'):
    book_id = int(input("Enter book id: "))
    membership_number = int(input("Enter you membership number: "))
    rentOrPurchase(id=book_id, membership_number=membership_number, type="purchase")
    
elif(user_choice == "6"):
    book_id = int(input("Enter book id: "))
    membership_number = int(input("Enter you membership number: "))
    returnRentedBook(membership_number=membership_number, book_id=book_id)
else:
    print("Invalid Choice")
