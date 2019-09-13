#===============gloabal===============
# v=100

# def fn():
#     global v
#     v=200
# fn()
# print("v= ", v)

#===============nonlocal===============
var=100
def f1():
    var=200
    print("var in f1 = ", var)
    def f2():
        nonlocal var
        var=300
        print("var in f2 = ", var)
    f2()
    print("var after f2() is ", var)    #after f2(), the v won't change, if we want to change the v in f2(), we can use non-local
f1()
print('global var =', var)