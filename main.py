# print("Hello world\n")
# this is comment
a=18
b="shital"
c=2.2
# print(a+3)
# converting int into float and string
a1=float(a)
a2=str(a)
# print(a1,a2)

# converting string into int and float
# b1=int(b) # can not convert sting into int and float
# b2= float(b)
# print(b1,"\n", b2)

# converting float into int and string
c1= int(c)
c2= str(c)
# print(c1,"\n", c2)

# string features
name= '''shital
    is good girl'''
# print(name)
# print(name[0])
# print(name[2:4])
# print(name[2:])
# print(name[:10])
name1="  shital  "
# print(name.strip())
# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.replace("i","ee"))

name2="siya"
var="This is a {} and she is good girl {}".format(name.strip(),name2.strip())
# print(var)
var="This is a {1} and she is good girl {0}".format(name.strip(),name2.strip())
# print(var)

# use of f string 
var="This is a {name1} and she is good girl {name2}"
# print(var)

var=f"This is a {name1} and she is good girl {name2}"
# print(var)

'''
Python Collection:
1. List
2. Tuple
3. Set
4. Dictionary

'''
# List
lst=[23,45,3,4,56,78]
lst2=type(lst)
lst2=lst[1]
# print(lst2)

lst2=lst[1:6]
# print(lst2)

lst2=lst[:5]
# print(lst2)

lst2=len(lst)
# print(lst2)

lst2=len(lst)
# print(lst2)

lst[3]=11
lst2=lst
# print(lst2)

lst.append(100)
# print(lst)

lst.insert(1,200)
# print(lst)

lst.pop()# removes the element from end
# print(lst)

lst.remove(23)
# print(lst)

del lst[2]
# print(lst)

# Tuple

a=("shital","siya",'kumar',"shital")
var=type(a)
# print(var)

# a[2]="akshya" #cannot change the elements
# print(a)

n=a.count("shital") # count(): Returns the number of times a specified value occurs in a tuple
# print(n)

n=a.index("shital")
# print(n)
n=a.index("kumar")
# print(n)

a=list(a)
var=type(a)
# print(var)

# Set

a={2,3,4,2,2,2,4,5,6,7}
# print(a)

a.add(90) # add(): used to add single element into a
# print(a)
a.update([23,45,56])
# print(a)

a.remove(2)
# print(a)
a.discard(122)
# print(a)

# Dictionary

shitDict={
    "name":"shital",
     "age":32,
     "sex":"female"

}

# print(shitDict)
# print(shitDict["name"])
 
shitDict.pop("age")
# print(shitDict)

shitDict.update({"age":32,"marks":444})
# print(shitDict)
del shitDict
# print(shitDict)

# age=input("Enter ur age\n")
# print(age, type(age))
# age=int(age)
# print(age, type(age))

#Function

def display():
    print("Hi Shital")
    print("Welcome to College")

# display()

# def sum(a,b):
#     return a+b

# print(sum(2,3))


# class

class Emp:
    def __init__(self):
        self.name="shital"
        self.age=34
        self.salary=23000

e=Emp()
print(e.name,"\n",e.age)
