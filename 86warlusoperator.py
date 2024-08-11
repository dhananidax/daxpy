#walrus operator:= assigns values to variables as part of a larger expression

#a=True
#print(a:=False)

'''num=[1,2,3,4,5] 

while(n:=len(num))>0:
    print(num.pop())'''

'''foods=list()  #without walrus operstor
while True:
    food=input("enter food:")
    if food=="quit":
        break
    foods.append(food)'''

foods=list()  #with walrus operator
while food:=input("enter food:")!="quit":
    foods.append(food)
    print(foods)