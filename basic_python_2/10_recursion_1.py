def fx(n):
    print("recursive to level", n)
    if n==3:
        return
    fx(n+1)
    print ("back to level", n)
fx(1)

print("program end !")