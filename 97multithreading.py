import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    time1=time.perf_counter()
#normal code
'''func(4)
func(2)
func(1)'''
'''calcuating total time
time2=time.perf_counter()

print(time2-time1) # 4+2+1 = 7 seconds total time taken by normal code '''

#same code using threads
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()

t1.join() #wait for the thread to finish itself before continuing the code in the program 
t2.join() #wait for the thread to finish itself before continuing the code in the program
t3.join() #wait for the thread to finish itself before continuing the code in the program

#calcuating total time'''
'''time2=time.perf_counter()

print(time2-time1)''' # 4+2+1 = 7 seconds total time taken by normal code 

def poolingDemo():
    with ThreadPoolExecutor() as executor:
     future=executor.submit(func,3)
     print(future.result()) 
     future=executor.submit(func,2)
     print(future.result()) 
     future=executor.submit(func,4)
     print(future.result()) 


poolingDemo() 
