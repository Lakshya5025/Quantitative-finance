from pathlib import Path
import os
path = Path("quant-week1/day6")
file_path = path / "grades.txt"

def unique_file_name(location, base, extension):
    name = location / f"{base}{extension}"
    counter = 1
    flag = False
    while(os.path.exists(name)):
        flag = True
        name = location / f"{base}{counter}{extension}"
        counter += 1
    return name
    

def append_to_file(students, total, highest, name):
    file_path = path / f"{name}.txt"
    if(os.path.exists(file_path)):
       with open(file_path, "r+", encoding="utf-8") as f:
            count = 0
            existing_students = ""
            existing_data = ""
            for line in f:
                if(count == 0): existing_students = line
                else: existing_data = line
                count += 1
            f.seek(0)      
            f.truncate() 
            newTotal = total
            newHighest = highest
            list_of_data = existing_data.strip().split(",")
            
            newTotal += int( list_of_data[0].split(":")[1])
            newHighest = int(list_of_data[1].split(":")[1]) if int(list_of_data[1].split(":")[1]) > newHighest else newHighest
            newAverage = (float(list_of_data[2].split(":")[1]) + (total / len(students)))/2
            existing_students = existing_students[:-1]
            for student in students : 
                existing_students += f"name:{student['name']} marks:{student['marks']},"
            f.write(existing_students + "\n")
            f.write(f"Total:{newTotal},Highest:{newHighest},Average:{newAverage}")
            print("compelete updating file")
    else:
        print("File is not present")
        print("Creating new file")
        create_new_file(students=students, total=total, highest=highest, base=name)


        
        

def create_new_file(students, total, highest, base = "grades"):
    average = total/len(students)
    file_path = unique_file_name(location=path, base= base, extension=".txt")
    with open(file_path, "w",encoding="utf-8") as f:
        for student in students:
            f.write(f"name:{student['name']} marks:{student['marks']},")
        f.write("\n")
        f.write(f"Total:{total},Highest:{highest},Average:{total/number_of_students}")

    


number_of_students = int(input("Enter the number of students: "))
students = []
total = 0
highest = 0
for i in range(number_of_students):
    name = input(f"Enter name of student {i + 1}: ")
    marks = int(input(f"Enter marks of student {i + 1}: "))
    total += marks
    if(marks > highest): highest = marks
    student = {"name": name, "marks" : marks}
    students.append(student)

print("OPTIONS:")
print("1: Create new file")
print("2: Append to existing file")
option = input("Choose from 1 or 2: ")
if(option == '1'):
    create_new_file(students=students,total=total, highest=highest, base="grades")
elif(option == '2'):
    file_name_input = input("Enter the file name(.txt extension only): ")
    name_seperation = file_name_input.split(".")
    file_name = ""
    if(len(name_seperation) == 1):
        file_name = name_seperation[0]
    else:
        if(name_seperation[len(name_seperation) - 1] != "txt"):
            file_name = file_name_input
        else:
            for i in range(len(name_seperation) - 1):
                file_name = file_name + name_seperation[i] + "."
            file_name = file_name[:- 1 ]
        
        
    append_to_file(students=students,total=total, highest=highest,name=file_name)
else:
    print("Invalid Option")

