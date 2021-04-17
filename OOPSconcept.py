class Employee:
    '''
    def __init__(self,fname,lname,sal):
        self.fname=fname
        self.lname=lname
        self.salary=sal
        self.increment= 1.2

    def increase(self,increment):
        self.increment= int(self.salary* self.increment)

shital=Employee("shital","patil",50000)
siya=Employee("siya","ajagekar",150000)
# print(shital,siya) ginves object address
print(shital.fname,shital.lname,shital.salary,"\n")
print(siya.fname,siya.lname,siya.salary)

shital.increase(1.5)
print(shital.__dict__ )

'''

    increment= 1.2
    no_of_emp=0
    def __init__(self,fname,lname,sal):
        self.fname=fname
        self.lname=lname
        self.salary=sal
        Employee.no_of_emp +=1

    def increse(self):
        self.increse= int( self.salary * Employee.increment)


print("No of employee  ", Employee.no_of_emp)
shital= Employee("shital","Patil",50000)
shital.increse()
print(shital.__dict__)
print("No of employee  ",Employee.no_of_emp)

harry=Employee("harry","sutar", 40000)
harry.increse()
print(harry.__dict__)
print("No of employee  ",Employee.no_of_emp)


# to check class variable use following
print(Employee.__dict__)

siya= Employee("siya","patil", 60000)
siya.imcrement=9
siya.increse()
print(siya.__dict__)