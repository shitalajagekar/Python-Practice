# USE OF STATIC METHOD WITH THE HELP OF @staticmethod DECORATOR


class Employee:
     
     @staticmethod
     def isOpen(day):

        if day=='sunday':
             return False
        else:
            return True

s=Employee()
print(s.isOpen('monday'))
print(Employee.isOpen('thuesday'))
