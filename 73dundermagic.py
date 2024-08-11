class employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"the name of the employee is {self.name}"
    
    def __repr__(self):
                return f"employee('{self.name}')"
    
    def __call__(self):
        print("hello")


#e=employee()   #  for lenth function
#print(e.name)  #  for lenth function
#print(len(e))  #  for lenth function

#create new python file and write below code   #for str function
'''from 73dundermagic import employee          #  for str function
e=employee("dax")                              #  for str function
print(str(e))                                   #  for str function
print(repr(e))                                #  for repr function
e()'''                                            #  for call function