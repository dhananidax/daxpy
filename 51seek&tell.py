with open('myfile1.txt','r') as f:
    print(type(f))
    #move to the 10th byte in the file
    f.seek(10) #starts from 10th byte
    #read the next 5 bytes
    print(f.tell())# tells the current position
    data=f.read(5)
    print(data)

with open('myfile2.txt','w') as f:
    f.write('hello dax')
    f.truncate(3)   #it will truncate the file to 3 bytes truncate means it will delete the data after 3 bytes

with open('myfile2.txt','r') as f:
    print(f.read())