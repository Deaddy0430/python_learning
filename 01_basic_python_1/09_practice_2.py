#..............example 1 combine................
# s = "ABC"
# s2 = "123"
# L = [x+y for x in s for y in s2]
# print(L)

#..............example 2 remove duplicates................
# L = [1, 3, 2, 1, 6, 4, 2, 98, 82]
# L2 = []
# for x in L:
#     if x not in L2:
#         L2.append(x)
# print(L2)

#..............example 3 fibonacci................
#1 1 2 3 5 8 13
#2=1+1; 3=1+2; 5=2+3 .....

#        method 1
# a=0
# b=1
# L=[]
# while len(L) < 40:
#     a,b = b, a+b
#     L.append(a)
# print(L)

#        method 2
L=[1,1]
while len(L) < 40:
    L.append(L[-1]+L[-2])

print(L)