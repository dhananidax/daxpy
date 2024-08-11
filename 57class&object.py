class person:
    name="dax"
    job="software developer"
    networth=50
    def info(self): #self is a reference to the current instance of the class & used to access the variables of that class
        print(f"{self.name} is a {self.job}")




a=person()  #object created
b=person()
a.name="dhanani"
a.job="clerk"
#print(a.name,a.job,a.networth)
a.info()
b.info()