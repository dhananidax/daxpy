#asyncio is used to run multiple tasks at the same time in python by using coroutines 

import time
import asyncio
import requests

async def function1():
    #time.sleep(3)
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico1", "wb").write(response.content)
    await asyncio.sleep(3)
    print("func 1")
    return "hello"

async def function2():
    #time.sleep(5)
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico2", "wb").write(response.content)
    await asyncio.sleep(5)
    print("func 2")

async def function3():
    #time.sleep(1)
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico3", "wb").write(response.content)
    await  asyncio.sleep(1)
    print("func 3")


async def main(): #main function
    #l=await asyncio.gather(function1(),function2(),function3()) #gather is used to run multiple tasks at the same time
    #print(l)
    #task=asyncio.create_task(function1())
    await function1()  #await is used to wait for the task to finish
    await function2()  #await is used to wait for the task to finish
    await function3()  #await is used to wait for the task to finish


asyncio.run(main()) # run the main function


#function1()
#function2()
#function3()

