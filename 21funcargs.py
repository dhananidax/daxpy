#def average(a=5,b=5):
#    print("average is",(a+b)/2)
#
#
def average(*numbers): # *numbers means it can take any number of arguements
    sum=0
    for i in numbers:
      sum=sum+i
#    print("average ",(sum/len(numbers)))
    return sum/len(numbers)
c= average(10,20,30)
print(c) #gives priority to this arguements

#def name(**name):
#    print(type(name))
#    print("hello,",name["mname"],name["age"],name["city"],name["country"])
#    
#    name(mname="dax",age="two",city="delhi",country="india")