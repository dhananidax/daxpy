#public,private,protected

'''class employee:
    def __init__(self):
        self.__name="dax" #to use private specifier (__) will be used

a=employee()
#print(a.__name)#cannot access private specifier directly
print(a._employee__name)# can be accessed indirectly
print(a.__dir__())  '''

class student:
    def __init__(self):
        self.name="dax" #underscore is not compulsory

    def _funname(self):  #protected method
        return "codewithdax"
    
class subject(student):  #innherited class
    pass

obj=student()
obj1=subject()
#calling by student obj
print(obj.name)             #underscore is not compulsory
print(obj._funname())
#calling by subject obj
print(obj1.name)
print(obj1._funname())



        