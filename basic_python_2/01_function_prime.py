def mymax(a, b):
    print('a =', a)
    print("b =", b)
    if a>b:
        print(a, ">", b)
    else:
        print(a, "<", b)
    print()

def isprime(x):
    if x <= 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prime_m2n(m, n):
    L=[]
    for i in range(m, n):
        if isprime(i):
            L.append(i)
    return L



# mymax(20, 30)
# mymax(100, 50)
# mymax("abc", "123")

L=prime_m2n(50, 300)
print(L)