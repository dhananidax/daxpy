#generators in python - yield keyword in python to create generators in python .it is used to create iterators in python

def my_generator():
    for i in range(100000):
        yield i
        #print("hello")

gen=my_generator()
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

for i in gen:
    print(i)