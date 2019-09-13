#==========Example 1===========
#求和1+2+3++...++100的和
def mysum(x):   #x cannot be 1000 because the max recursive level for python is 1000
    if x<=1:
        return 1
    return x + mysum(x-1)
v=mysum(100) 
#print(v)

#==========Example 2==========
#求阶乘： n！= 1 x 2 x 3 xx...x (n-1) x n
def myfac(x):
    if x<=1:
        return 1
    return x * myfac(x-1)
print(myfac(5))