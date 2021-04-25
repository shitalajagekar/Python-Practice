
# We must be comfortable with the fact that everything in Python (Yes! Even classes), are objects. 
# Names that we define are simply identifiers bound to these objects. Functions are no exceptions,
#  they are objects too (with attributes). Various different names can be bound to the same function object.


"""def first(msg):
    print(msg)

first("Hello")
second=first
second("Hello2")"""

'''def inc(x):
    return x+1

def dec(x):
    return x-1

def operation(fun, x):
    val=fun(x)
    return val

data=operation(inc,12)
print(data)

data=operation(dec,12)
print(data)
'''

# A function can return another function

'''def is_called():
    def is_returned():
        print("Inside Return function")

    return is_returned

new=is_called()
new()'''

#  use of decorator
def smart_divide(fun):
    def inner(a,b):
        print(" I am going to divide a and b")
        if b==0:
            print("we can not divide")
            return

        else: 
            return fun(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b


print(divide(24,3))


        
