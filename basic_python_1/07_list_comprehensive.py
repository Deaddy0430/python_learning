n = int (input("please enter the tree's height: "))


for i in range(1, n+1):
    num_blank=n-i
    print(" "*num_blank + "*"*(2*i-1))

for i in range(1, n+1):
    print(" "*(n-1) + "*")