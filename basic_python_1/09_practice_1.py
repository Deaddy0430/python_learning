#Narcissistic Number: (find all this kinds of number fromm 100~999)
#example: 153 = 1**3 + 5**3 + 3**3

#................method 1............................
# for x in range(100, 1000):
#     digit_3 = x//100
#     digit_2 = x%100//10
#     digit_1 = x%10
#     if x == digit_3**3 + digit_2**3 + digit_1**3:
#         print (x)

#................method 2............................
# for x in range(100,1000):
#     s=str(x)
#     digit_3 = int(s[0]) 
#     digit_2 = int(s[1]) 
#     digit_1 = int(s[2]) 
#     if x == digit_3**3 + digit_2**3 + digit_1**3:
#         print (x)

#................method 3............................
for digit_3 in range(1, 10):
    for digit_2 in range(10):
        for digit_1 in range (10):
            x = 100*digit_3 + 10*digit_2 + digit_1
            if x == digit_3**3 + digit_2**3 + digit_1**3:
                print (x)           