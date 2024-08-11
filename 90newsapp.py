import requests
import json
query=input("what type of news are you interested in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-04-20&sortBy=publishedAt&apiKey=8c4ca85852214055ad07b1a817307450"
r=requests.get(url)
news=json.loads(r.text)
for i in news['articles']:
    print(i['title'])
    print(i['description']) 
    print("-------------------------")
#print(r.text)