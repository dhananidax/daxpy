dic={
    "name":"dax",
    "age":22,
}
#print(dic)
#print(dic.keys())
#print(dic.values())
#print(dic["name"],dic["age"])

for key in dic:
    #print(key,dic[key])
    print(f"the key is {key} and value is {dic[key]}")

print(dic.items())
for key,value in dic.items():
    print( f"the key is {key} and value is {value}")