class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showdetails(self):
        print(f"the name of employee: {self.id} is {self.name}")

class programmer(employee):
    def showlang(self):
        print("the default language is python")


e=employee("dhanani dax",400)
e.showdetails()
e1=programmer("dhanani",500)
e1.showdetails()
e1.showlang()