class employee:
    company="Apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def changecompany(cls,newcompany): #cls is a reference to the class and used to access the variables of that class
        cls.company=newcompany  #cls ki jagah kuch bhi likh skte hai like self,tinde whatever we want 

e=employee()
e.name="dax"
e.show()
e.changecompany("amazon")
e.show()
print(employee.company)