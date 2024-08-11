#a=int(input("enter your age: "))
#if a>=18:
#    print("You are eligible for vote")
#else:
#    print("not eligible for vote")

#--------------------elif
# a=int(input("enter your number: "))
# if (a>0):
    # print("no. is positive")
# elif(a<0):
    # print("no. is negative")
# else:
    # print("no. is zero")

#--------------------nested if
a=int(input("enter your number: "))
if (a<0):
    print("no. is negative")
elif(a>0):
     if(a<5):
        print("no. is less than 5")
     elif(a>5 and a<15):
        print("no. is between 5 and 15")
     else:
        print("no. is greater than 15")
else:
    print("no. is zero")






