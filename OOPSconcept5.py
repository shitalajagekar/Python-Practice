# to convert function into attribute with the help of of @property decorator and change the value of it's parameter
#  using @(name).setter and delete it's value using deleter

class Employee:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname= lname

    @property
    def email(self):
        if self.fname==None and self.lname==None:
            return "Email do not set"
        else:
            return self.fname + "."+ self.lname + "@gmail.com"

    @email.setter
    def email(self,givenmail):
        split_id=givenmail.split('@')[0].split('.')
        self.fname= split_id[0]
        self.lname=split_id[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


Neha = Employee("Neha", " Chavan")
Neha.email="Chavan.Neha@gmail.com"
print(Neha.email)

del Neha.email
print(Neha.email)