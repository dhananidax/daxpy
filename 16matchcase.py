x=int(input("Enter value of x"))
match x:
    case 0:
        print("value is 0")
    case 4:
        print("value is 4")
   # case _ if x!=90:
   #     print(x,"is not 90")
    case _ if x>10 and x<20:
        print ("value is between 10 and 20")
    case _ :
        print(x)
