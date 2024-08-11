class animal:
    def __init__ (self,name,species):
        self.name=name
        self.species=species

    def makesound(self):
        print("generic animal sound")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed=breed
    def makesound(self):
        print("bark")

d=dog("dax","lab")
d.makesound()

a=animal("dax","dog")
a.makesound()
