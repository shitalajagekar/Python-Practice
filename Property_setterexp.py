#  use of @property decorator and setter ()

class year_graduated:
   def __init__(self, year=32):
      self._year = year

   @property
   def Aboutyear(self):
      return self.__year

   @Aboutyear.setter
   def Aboutyear(self, a):
      self.__year = a

grad_obj = year_graduated()
print(grad_obj._year)

grad_obj.year = 2018
print(grad_obj.year)