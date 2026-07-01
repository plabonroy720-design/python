class Father:
    def __init__(self, name):
        self.name=name

    def father(self):
        print(f'The father name is : {self.name}')



class Mother:
    def __init__(self, mname):
        self.mname=mname

    def mother(self):
        print(f'the mother name is : {self.mname}')


class Child(Father, Mother):                #note down
    def __init__(self,name,mname,sname):    #note down
        Father.__init__(self,name)          #note down
        Mother.__init__(self,mname)         #note down
        self.sname=sname

    def Show_info(self):
        Father.father(self)                 #note down
        Mother.mother(self)                 #note down
        print(f'my name is {self.sname}')


a=Child(
    input("Enter the name of the father : "),
    input("Enter the name of the mother : "),
    input("Enter the name of the child : ")
)
a.Show_info()
