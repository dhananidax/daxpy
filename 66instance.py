class employee:
    companyname="Apple" #class variable
    noofemployees=0
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.raise_a=0.02
        employee.noofemployees+=1 
    def showdetails(self):
        print(f"the name of employee: {self.id} is {self.name} and the raise of {self.noofemployees} from {self.companyname} is {self.raise_a}")

e=employee("dax",400)
e.raise_a=0.03
e.companyname="Amazon"
e.showdetails()
employee.companyname="Google" #class variable can be changed 
e1=employee("dax1",401)
e1.showdetails()
#employee.showdetails(e) #instance