#a=input("enter value of a")
#print(f"multiplication table of {a} is:")
#try:
#    for i in range(1,11):
#     print(f"{int(a)} * {i} = {int(a)*i}")
#except:  #or except Exception as e:
#    print ("ERROR")
#
#    print("some imp lines")

try:
    a=int(input("enter value of a"))
    b=int(input("enter value of b"))
    print(a/b)
except ZeroDivisionError:
    print("b can not be zero")
except ValueError:
    print("a and b should be integer")
    