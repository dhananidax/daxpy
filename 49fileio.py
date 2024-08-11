#f=open('myfile.txt','r') #open file in read mode
#f=open('myfile.txt')#open file in default mode
#f=open('myfile.txt','rb') #binary mode
#print(f)
#text=f.read()
#print(text)
#f.close()

#-----writing mode ------
#f=open('myfile1.txt','w')
#f=open('myfile1.txt','a') #append mode adds content in the file
#f.write("hello dhanani")
#f.close()

with open('myfile1.txt','a') as f:  #other way of apending file
    f.write("hello dax")     