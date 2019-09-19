def func(*args):
    print("the number of args are: ", len(args))
    print("args=", args)

# func(1,2,3,4)
# func("hello", "world", 1,2,3)

def mysum(*args):
    s=0
    for x in args:
        s+=x
    return s

# print(mysum(123,22,21))
# print(mysum(123,22,21,324,11))

#--------------star dic kwarg-----------------
def func2(**kwargs):
    print("the number of args are: ", len(kwargs))
    print("kwargs = ", kwargs)

func2(name="Ethan", age=23)


