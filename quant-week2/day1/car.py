class Car:
    def __init__(self, name, man_year):
        self.name = name
        self.man_year = man_year
    def details(self):
        print(f"{self.name} was manufactured in {self.man_year}")
    def start(self):
        print(f"{self.name} has been started")
        
a = Car("a", 1999)
print(a.name)
print(a.man_year)
a.start()
a.details()