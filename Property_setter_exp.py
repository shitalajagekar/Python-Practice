# Example and information about @property and setter method

class Division:

    def __init__(self,d):

        self._diviser=d   # Private variable of class Division

    @property
    def diviser(self):

        return self._diviser
## the attribute name and the method name must be same which is used to set the value for the attribute
    @diviser.setter
    def diviser(self,n):
        if (n>1) :
            self._diviser=n
        else: 
            self._diviser=1

d= Division(5)
d.diviser=6
print(d.diviser)




