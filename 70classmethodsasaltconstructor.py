class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromstring(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
e=employee("dax",1000)
print(e.name)
print(e.salary)
string ="john-1000"
e1=employee.fromstring(string)
print(e1.name)
print(e1.salary)