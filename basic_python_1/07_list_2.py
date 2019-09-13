L=[]

while True:
    s=input("please input a string: ")
    if not s:   #not: s has nothing
        break
    L.append(s)

s=0
L.reverse()
for line in L:
    print(line)
    s+=len(line)

print("There are %s characters" % s)