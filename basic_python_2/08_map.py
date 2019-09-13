# def pow2(x):
#     return x**2

# for x in map(pow2, range(1,5)):
#     print(x)

# for n in map(pow, range(1,10), range(4,0,-1)):
#     print(n)

#==========practice=============
#1. 1**2 + 2**2 + 3**2........+9**2
print("pow2 total is: ",sum(map(lambda x: x**2, range(1,10))))

#2. 1**3 + 2**3 + 3**3........+9**3
total=0
pow3=lambda n: n**3
for x in map(pow3, range(1,10)):
    total+=x
print("pow3 total is: ", total)

#3. 1**9 + 2**8 + 3**7........+9**1
total=0
for x in map(pow, range(1,10), range(9,0,-1)):
    total+=x
print("pow total is: ", total)