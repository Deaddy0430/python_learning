class Human:
    count = 0   #this is the class variable

print("human's variable is", Human.count)
h1 = Human()
print("human's vairable in h1 object is", h1.count)
h1.count = 100
print(h1.count)
print(Human.count)

h1.__class__.count += 1
print("h1 =", h1.count)
print("Human =", Human.count)