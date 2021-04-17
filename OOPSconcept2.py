# USE OF CLASS METHOD WITH THE HELP OF @classmethod DECORATOR

class Employee:
    increment= 1.2
    no_of_emp=0
    def __init__(self,fname,lname,sal):
        self.fname=fname
        self.lname=lname
        self.salary=sal
        Employee.no_of_emp +=1

    def increse(self):
        self.increse= int( self.salary * Employee.increment)


    @classmethod
    def change_increse(cls,amount):
        cls.increment=amount

shital=Employee("shital","patil",5000)
Employee.change_increse(2)
shital.increse()
print(shital.__dict__)