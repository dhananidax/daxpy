class person:
    def __init__(self,n,o):   #constructor created using init
        print("hey i am dax")
        self.name=n
        self.job=o



    #name="dax"
   # job="software developer"

    def info(self):
        print(f"{self.name} is a {self.job}")

a=person("dax","data science")
b=person("dhanani","hr")
#print(a.name)
#a.name="dhanani"
#a.job="hr"
a.info()
b.info()