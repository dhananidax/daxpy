tup=(1,5,76,"dax","dhani",600)
print(tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[0:3])
print(tup[2:])
print(tup[1:4:2])#2 represents gap between 1 and 4
if "dhani" in tup:
    print("yes")
else:
    print("no")


tup2=tup[1:4]
print(tup2)
'''for i in tup:
    tup2=tup+tup
    print(tup2)'''