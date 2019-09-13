L=[3,5]
L[0:0]= [1,2]
L[3:3]= [4]
L[len(L):len(L)]=[6]
print(L)

L[:]=L[::-1]
print(L) 