class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,other):
        i=self.i+other.i
        j=self.j+other.j
        k=self.k+other.k
        return vector(i,j,k)


v=vector(1,2,3)
print(v)
v1=vector(4,5,6)
print(v1)

print(v+v1)
print(type(v+v1))