#=========================filter===========================
# def isodd(x):
#     return x%2==0
# for x in filter(isodd, range(10)):
#     print(x)

#===============practice================
#1. find the even number from 1 - 20 by using filter
even=[x for x in filter(lambda x: x%2==0, range(1,21))]
print (even)

#2. find the prime number from 1-100 by using filter
def isprime(x):
    if x<=1:
        return False
    for k in range(2,x):
        if x%k==0:
            return False
    return True

prime=list(filter(isprime, range(100)))
print(prime)


#=========================sorted===========================
# L=[5,-1,-4,0,3,1]
# L2=sorted(L)
# L3=sorted(L,reverse=True)
# L4=sorted(L,key=abs)

# print("L2: ", L2)
# print("L3: ", L3)
# print("L4: ", L4)
#===============practice================
names=['Ethan', 'Phoebe', 'David','Kyle','Emily']
names2=sorted(names)
names3=sorted(names,key=len)
print(names3)