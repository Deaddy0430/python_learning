L=["ethan", "david", "phoebe"]
d={x:len(x) for x in L}
print(d)

Nos = [1001, 1002, 1003, 1004]
name = ["Ethan", "David", "Phoebe", "Kyle"]
d={Nos[i]:name[i] 
    for i in range(min(len(Nos),len(name)))}

print(d)