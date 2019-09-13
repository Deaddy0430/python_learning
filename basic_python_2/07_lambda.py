#========================example 1======================
#check a number if it can perfectly divide by n^2+1
fx = lambda n: (n**2+1)%5==0
k=int(input("please enter a number: "))
print(fx(k))

#========================example 2======================
findMax = lambda x,y: max(x,y)
print(findMax(100,200))