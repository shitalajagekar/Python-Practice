# use of setter deleter and property decorator

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.extention="email.com"

    @property
    def email(self):

        if self.fname==None or self.lname==None or self.extention==None:
            return "Do not set email..."
        return f"{self.fname}.{self.lname}@{self.extention}"


#  If we want to change the value of email by assigning string to it then we need setter for this

    @email.setter
    def email(self,string):
        name=string.split("@")[0]
        ext=string.split("@")[1]
        self.fname= name.split(".")[0]
        self.lname= name.split(".")[1]
        self.extention=ext
# if i want to delete the email value then we need deleter as follows:
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        self.extention=None


shital=Person("Shital","Ajagekar")
print(shital.email)
shital.email="siya.patil@gmail.com"
print(shital.email)

#  use of deleter

del shital.email
print(shital.email)




    