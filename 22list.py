#l=[1,2,3,4,5]
#print(type(l))
l1=["dax","dhani","dhanani",1,5.4,5+4j]
#print(l1[0]) #indexing
#print(l1[1]) 
#print(l1[5-3]) #slicing
#print(l1)
if 1 in l1:
    print("yes")
else:
    print("no")
    #samething applies for string
#if "dax" in l1:
#
#     print("yes")
#
# else:
#
#     print("no")
print(l1[1:3])
print(l1[1:])
print(l1[:3])
print(l1[-1])
print(l1[-3:-1])
print(l1[0:6:2])
print(l1[0:6:3])

lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]
print(lst)