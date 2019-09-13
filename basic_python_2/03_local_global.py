a=1
b=2
c=3

def f1(c,d):
    e=300
    print("local() is ", locals())
    print("---------------------------")
    print("global() is ", globals())

    for k,v in globals().items():
        print(k, '-->', v)
    
    print(c)    #this c is local c, 300
    print(globals()['c'])   #this c is glocal c, 3

f1(100,200)