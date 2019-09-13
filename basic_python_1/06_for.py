string=input("please enter a string: ")
counter=0
for ch in string:
    if ch == ' ':
        counter+=1
else:
    print("There are %d spaces" %counter)