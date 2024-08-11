'''class parent:
    def parent_method(self):
        print("parent method")

class child(parent):
   def parent_method(self):
       print("parent method2")
       super().parent_method()
   def child_method(self):
        print("child method")
        super().parent_method()

c=child()
c.child_method()
c.parent_method()'''

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class programmer(employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language=language
   

e=employee("dax",400)
f=programmer("dhanani",500,"python")
print(f.name)
print(f.id)
print(f.language)