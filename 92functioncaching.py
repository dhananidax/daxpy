from functools import lru_cache
import time

@lru_cache(maxsize=None) # function caching 
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(61))
print("done for 61")

'''function caching is used to speed up the program by reducing the number of calls to the function in the program 
when the same arguments are passed again and again in the program to the function '''
