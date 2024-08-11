x=4
y=50
print(x)


def fun():
    global x
    x=5
    print(f"the global y is {y}")
    print(f"the local x is {x}")
    print("hello dax")

print(f"the global x is {x}") #global variable(x)
fun()
#x=10
print(f"the global x is {x}")