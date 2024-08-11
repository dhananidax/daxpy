'''x=(1,2,3) #x=[1,2,3]
print(dir(x))
print(x.__add__)'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1

p=person("dax",22)
print(p.__dict__)

print(help(person))  #help of class 