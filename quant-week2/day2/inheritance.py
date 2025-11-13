class Person:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}")
class Employee(Person):
    def __init__(self, name, company, salary):
        super().__init__(name)
        self.company = company
        self.salary = salary
    def employee_details(self):
        print(f"{self.name} is a employee of {self.company} has a salary of {self.salary}")
    
class Manager(Employee):
    def __init__(self, name, company, salary, departmant):
        super().__init__(name, company, salary)
        self.departmant = departmant
        
    def manager_details(self):
        print(f"{self.name} is the manager of {self.departmant} department in {self.company} have a salary of {self.salary} ")
        

development_manager = Manager("lakshya", "xyz", 2900000, "innovation")

development_manager.speak()
development_manager.employee_details()
development_manager.manager_details()
