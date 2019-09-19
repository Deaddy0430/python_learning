height=int(input("please enter the square height: "))

for x in range(1,height+1):
    for y in range(x, x+height):
        print("%2d" % y,end=' ')
    print()