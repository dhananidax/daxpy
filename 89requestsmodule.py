import requests
from bs4 import BeautifulSoup
'''response=requests.get("https://www.google.com")
print(response.text)'''

url="https://www.jetbrains.com/pycharm/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)








'''url="https://jsonplaceholder.typicode.com/posts"

data ={
    "title":"dhanani",
    "body":"data science",
    "id":101
}
headers={
    "Content-type":"application/json"
}
response=requests.post(url,headers=headers,json=data)
print(response.text)'''