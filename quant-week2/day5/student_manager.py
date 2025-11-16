import os
import json

base = os.getcwd()
data_dir = os.path.join(base, "quant-week2\\day5")
file_path = os.path.join(data_dir, "students.json")

def ensure_file():
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)

class Student():
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        
        
def convert_into_json(student_object):
    name = student_object.name
    age = student_object.age
    marks = student_object.marks
    return {
        "name" : name,
        "age" : age,
        "marks" : marks
    }

def append_to_student_json(student_object):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        data.append(convert_into_json(student_object=student_object))

    with open (file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Student added successfully")

def search_to_student_json(student_name):
    flag = False
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for student in data:
            if(student["name"].lower() == student_name.lower()):
                flag = True
                break
    if(flag):
        print("Student found")
        return True
    else:
        print("Student not found")
        return False
        

def delete_student(student_name):
    if(search_to_student_json(student_name=student_name)):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        new_students = []
        for student in data:
            if(student['name'].lower() != student_name.lower()):
                new_students.append(student)
        with open (file_path, "w", encoding="utf-8") as f:
            json.dump(new_students, f, indent=2)
        print("Student removed successfully")


ensure_file()
print("What operation you want to perform:\n1.Add student\n2.Remove Student\n3.Search Student")

user_choice = input("Enter you choice : ")

if(user_choice == '1'):
    student_name = input("Enter the new student name : ")
    student_age = int(input("Enter the student age : "))
    student_marks = int(input("Enter the student marks : "))

    new_student_object = Student(name=student_name,age=student_age, marks=student_marks)
    append_to_student_json(new_student_object)
elif(user_choice == '2'):
    student_name_to_delete = input("Enter the student you want to remove : ")
    delete_student(student_name_to_delete)
    
elif(user_choice == '3'):
    student_name_to_search = input("Enter the student you want to serach : ")
    search_to_student_json(student_name_to_search)
else:
    print("Invalid choice")

        