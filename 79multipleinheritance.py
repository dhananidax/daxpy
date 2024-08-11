class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")

class dancer:
    def __init__(self,dance): 
        self.dance=dance
    def show(self): 
        print(f"the dance is {self.dance}")

class danceremployee(employee,dancer):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance

e=danceremployee("dax","kathak")
print(e.name)
print(e.dance)
e.show()
print(danceremployee.mro()) #mro is method resolution order 