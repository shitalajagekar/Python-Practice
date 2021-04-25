
## Next example of getter setter method:
# here we create private variable of class by preciding 2 underscore

class Graduate:
    def __init__(self,y=2010):
        self._year=y # private variable year precided by  underscore
# getter method
    def get_year(self):

        return self.__year
# setter method
    def set_year(self,y):
        self.__year=y

g= Graduate()
g.set_year(2011)
print(g._year)

g.year=2011
print(g.year)
