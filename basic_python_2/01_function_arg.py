def myfun(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    
myfun(1, 2, 3)

myfun(b=10, a=20, c=30)

s=[100,200,300]
myfun(*s)

d={"c":11, "b":22, "a":33}
myfun(**d)