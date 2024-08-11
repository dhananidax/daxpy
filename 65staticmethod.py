class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,a):
        self.num+=a

    @staticmethod
    def add(a,b):
        return a+b
    
#result=math.add(10,20)
#print(result)
a=math(10)
print(a.num)
a.addtonum(20)
print(a.num)


print(math.add(20,20))