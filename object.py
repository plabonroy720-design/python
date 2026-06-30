class Student:
    def __init__(self, name,age, cgpa):
        self.name=name
        self.age=age
        self.cgpa=cgpa
    def function(self):
        return f'My name is : {self.name} my age is {self.age} my cgpa is {self.cgpa}'
    def update(self, update_):
        self.cgpa=update_
        return f'My name is : {self.name} my age is {self.age} my NEW cgpa is {self.cgpa}'
s=Student(input("Enter the name of the student : "), int(input("Enter the age of the student : ")), float(input("Enter the cgpa of the stufent : ")))
print(s.function())
print(s.update(float(input("Enter the new cgpa : "))))