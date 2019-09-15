def make_power(y):  #the y comes from outside
    def fx(arg):
        return arg**y   #if the inside y is not used, this y will be kept 
    return fx
pow2 = make_power(2)
print('3^2 is: ', pow2(3))

pow2 = make_power(3)
print('3^3 is: ', pow2(3))