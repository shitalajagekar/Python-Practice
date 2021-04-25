#  
# WE use getter and setter method because because we want to hide the attributes of a object class 
# from other classes so that no accidental modification of the data happens by methods in other classes.

class Graduate:
    def __init__(self,y=2010):
        self.year=y
# getter method
    def get_year(self):

        return self.year
# setter method
    def set_year(self,y):
        self.year=y

g= Graduate(0)
g.set_year(2011)
print(g.year)


