class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def show_info(self):
        print(f'Name : {self.name} age : {self.age}')
class Student(Person):
    def __init__(self,name, age, department, cgpa):
        super().__init__(name, age)
        self.department=department
        self.cgpa=cgpa
    def show_student(self):
        print(f'Name : {self.name} age : {self.age} Department : {self.department} cgpa : {self.cgpa}')
    def update(self,s):
        self.cgpa=s
        print("We have updated the cgpa")
        print(f"The current cgpa is : {self.cgpa}")
    def check_result(self):
        if self.cgpa>=2.5:
            print("You have passed")
        else:
            print("Failed")
s=Student(
    input("Enter the name of the student : "),
          int(input("Enter the agae : ")),
          input("The department : "),
          float(input("Enter the cgpa : ")))
s.show_info()
s.show_student()
s.update(float(input("Enter the new cgpa : ")))
s.check_result()