#cou=("spain","france","india","australia","brazil")
#r=cou.count("india")
#print(r)

tup=(0,1,2,3,2,31,1,3,2,3)
#res=tup.count(3)
#res=tup.count(3)+tup.count(2)
#res=tup.index(3)
res=tup.index(3,4,8) #4 is start index, 8 is end index
print("total count:",res)