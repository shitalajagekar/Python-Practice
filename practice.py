
"""
class Parent:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def display(self):
        print("Name : ",self.fname," ", self.lname)

class Student(Parent):
    def __init__(self,fname,lname,rno,age):
        Parent.__init__(self,fname,lname)
        self.rno=rno
        self.age=age

    def display(self):
        Parent.display(self)
        print("Roll no : ",self.rno," Age of Student : ",self.age)




p=Student("shital","dhaku",3,23)
p.display()
"""

# same work with the help of SUPER() function

class Parent:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def display(self):
        print("Name : ",self.fname," ", self.lname)

class Student(Parent):
    def __init__(self,fname,lname,rno,age):
        super().__init__(fname,lname)
        self.rno=rno
        self.age=age

    def display(self):
        super().display()
        print("Roll no : ",self.rno," Age of Student : ",self.age)




p=Student("shital","dhaku",3,23)
p.display()
