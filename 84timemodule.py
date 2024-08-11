import time
def usingWhile():
    i=0
    while i<50000:
        i=i+1
        print(i)

def usingFor():
    for i in range(50000):
        print(i)

#init=time.time() #initial time
#usingFor()
#t1=time.time()-init #time taken by for loop
#usingWhile()
#print(time.time()-init)#time taken by while loop
#print(t1)#time taken by for loop

#print(4)
#time.sleep(3)#3 seconds delay
#print("this is printed after 3 seconds")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d ]]%I:%M:%S %p",t)
#formatted_time=time.asctime(t)  #or time.ctime() for ctime format and time.strftime("%I:%M:%S %p") for time format
print(formatted_time)