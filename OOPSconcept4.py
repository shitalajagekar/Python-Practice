# Class INHERITANCE

class Employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    increment=1.5
    def increase(self):
        self.salary= int(self.salary * Employee.increment)

class Programmer(Employee):
    def __init__(self,fname,lname,salary,lagn,exp):
        super().__init__(fname,lname,salary)
        self.language=lagn
        self.experience=exp

    def increase(self,):
        self.salary= int(self.salary * (self.increment + 0.2))



p= Programmer("shital","siay",20000,"python",2)
print(p.experience)
p.increase()
print(p.salary)