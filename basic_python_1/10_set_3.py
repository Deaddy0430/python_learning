names=["Ethan", "Zac", "Phoebe", "Kyle","David"]
s=set(names)
L=[]
for n in s:
    info = n + " Attendance: "
    r=input(info)
    if r != 'y':
        L.append(n)

print("These students did not attend: ")
for n in L:
    print(n, end=" ")
    print()