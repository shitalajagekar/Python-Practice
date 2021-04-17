# USE OF CLASS METHOD AS AN ALTERNATIVE CONSTRUCTOR

class Employee:

    def __init__(self,fname,lname,sal):
        self.fname=fname
        self.lname=lname
        self.salary=sal


    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)

shital=Employee.from_str("shital-Ajagekar-100000")
print(shital.__dict__)
        