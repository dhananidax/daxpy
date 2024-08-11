import os
    #os.mkdir("data")  creates directory
#if(not os.path.exists("data")):  if folder is not created then it retirns true
   # os.mkdir("data")

#for i in range(0,10):
    #os.mkdir(f"data/Day{i+1}")  creates multiple folder
    #os.rename(f"data/Tutorial  {i+1}",f"data/Day{i+1}")  rename the folder name

'''folder=os.listdir("data")   
print(folder)           prints all the folder of the data
for folders in folder: 
    print(folders)
    print(os.listdir(f"data/{folders}"))'''

print(os.getcwd()) #shows your present directory
#os.chdir("/Users")  changes directory of your current directory
 