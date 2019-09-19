#Question 1
#def myfun(a,b)
# 1. print out the max value
# 2. print out the sum
# 3. print out the product
# 4. print out all the even number from a to b

def myfun(a, b):
    L =[a, b]
    even=[]
    print("the max value is: ", max(L) )
    print("the max value is: ", sum(L) )
    print("the max value is: ", a*b)

    for x in range(a,b+1):
        if x%2==0:
            even.append(x)
    print("all the even number from a to b are: ", even)

#myfun(4,100)


#Question 2
# A monkey has a lot of peaches
#  day1: eat half of the total peaches, and eat an extra one after that
#  day2:  eat half of the current total peaches, and eat an extra one after that
#  .
#  .
#  .
#  day10: only one remains

# how many peaches the monkey initially had? 

def get_lastday(today_peaches):
    yesterday_peaches = today_peaches*2+1
    return yesterday_peaches

# today=1
# counter=1
# while counter<=10:
#     yesterday=get_lastday(today)
#     today=yesterday
#     counter+=1
# print("the monkey initially had %d peaches" % today)


#Question 3
# perfect number:
# 1+2+3=6
# 1x6=6
# 2x3=6
#a number is equal to the sum of all of its factors

# method 1 
# i=1
# while True:
#     L=[]
#     for x in range(1,i):
#         if i%x==0:
#             L.append(x)

#     if sum(L)==i:
#         print(i, "is perfect number")
#     i+=1

# method 2
def isPerfectNumber(i):
    L=[]
    for x in range(1,i):
        if i%x==0:
            L.append(x)
    if sum(L)==i:
        return True
    return False

def main():
    i=1
    while True:
        if isPerfectNumber(i):
            print(i, "is perfect number")
        i+=1

main()