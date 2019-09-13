def info(name, age=1, address="none"):
    print(name, "'s age is: ", age, " Address: ", address)

# info('Ethan', 23)
# info('Phoebe', 23, 'church ave')

def mysum(x,y,z=None):
    if z is None:
        return x+y
    return(x+y)%z

# print (mysum(4,6), mysum(4,6,3))

def myrange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    L=[]
    i=start
    while i<stop:
        L.append(i)
        i+=step
    return L
L=myrange(3)
print(L)

L=myrange(3,6)
print(L)

L=myrange(1,10,3)
print(L)