class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def showdetails(self):
        print(f"the name of the animal is {self.name} and the species is {self.species}")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed=breed

    def showdetails(self):
        animal.showdetails(self)
        print(f"the breed of the dog is {self.breed}")

class goldenretriever(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,breed="goldenretriever")
        self.color=color

    def showdetails(self):
        dog.showdetails(self)
        print(f"the color of the dog is {self.color}")

o=goldenretriever("shekar","black")
o.showdetails()   #use mro() to know the order of inheritance