class Person:
    def __init__(self, name):
        self.name=name
    def show_person(self):
        print(f"the name of the person is : {self.name}")
class Student(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department=department
    def show_student(self):
        super().show_person()
        print(f'the department is : {self.department}')
class CSEstudent(Student):
    def __init__(self, name, department, cgpa):
        super().__init__(name, department)
        self.cgpa=cgpa
    def show_cse(self):
        super().show_student()
        print(f'my cgpa is {self.cgpa}')
a=CSEstudent(
    input("Enter the name of the student : "),
    input("Enter the name of the department : "),
    float(input("Enter the cgpa of the student : "))
)
a.show_cse()
