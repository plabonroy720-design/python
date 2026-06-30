class Student:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def info1(self):
        print(f'Name is {self.name} age is {self.age}')
class Student_ex(Student):
    def __init__(self,name, age, department):
        super().__init__(name, age)
        self.department=department
    def print_info(self):
        print(f'name is {self.name} age is {self.age} and the department is {self.department}')
s=Student_ex(input("Enter the name of the student : "), 
             int(input("Enter the age : ")),
             input("Enter the name of the department : "))
s.print_info()