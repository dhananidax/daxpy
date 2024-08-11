#def cube(x):
 #   return x*x*x

#print(cube(2))
from functools import reduce  #to use reduce we have to import it only for reduce function
l=[1,2,3,4,5]
#newl=[]
#or items in l:
#   newl.append(cube(items))

#MAP
newl=list(map(lambda x:x*x*x,l))   
print(newl)

#FILTER

def fil(a):
    return a>2

newnewl=list(filter(fil,l))
print(newnewl)

#REDUCE
def mysum(x,y):
    return x+y
sum=reduce(mysum,l)
print(sum)  #1+2+3+4+5=15 b'coz we return x+y 