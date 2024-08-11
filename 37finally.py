def fun():
  try:
    l=[1,2,3,4,5]
    i=int(input("enter index"))
    print(l[i])
    return 1
  except:
    print("error")
    return 0

  finally:     #if you use in function then it works better than using indentation ,identation will not print but finally will print
    print("bye")

d=fun()
print(d)