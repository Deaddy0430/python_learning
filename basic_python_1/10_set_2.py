L = []
while True:
    s = input("please enter a word: ")
    if not s:
        break
    L.append(s)

# set method
# s = set(L)  #set can directly remove the duplicates
# print("The total number of types of words you entered is: ", len(s))

# for word in s:
#     print(word)

# list method
# L2 = []
# for x in L:
#     if x not in L2: # if x not in L2, implying that the x is the first time appeared
#         L2.append(x)
# for x in L2:
#     print(x)

s = set(L)
for x in L:
    if x in s:
        print(x)
        s.discard(x)