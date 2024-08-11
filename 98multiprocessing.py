import multiprocessing
import requests
import concurrent.futures

def downloadfile(url,name):
        print(f"started downloading file {name}")
        response = requests.get(url)
        open(f"files/file{name}.jpg", "wb").write(response.content)
        print(f"finished downloading file {name}")
  

if __name__=="__main__":
    url="https://picsum.photos/200/300"
'''pros=[]
for i in range(5):
   # downloadfile(url,i)
     p=multiprocessing.Process(target=downloadfile,args=[url,i])
     p.start()
     pros.append(p)

for p in pros:
    p.join()'''

with concurrent.futures.ProcessPoolExecutor() as executor: 
     l1=[url for i in range(5)]
     l2=[i for i in range(5)]
     results=executor.map(downloadfile,l1,l2)
     for result in results:
        print(result)