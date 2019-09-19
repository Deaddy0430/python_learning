fmt="name: %s , age: %d "
name=input("please enter your name: ")
age=int(input("please enter your age: "))
s = fmt % (name, age)
print(s)

s1=input("please enter the 1st line: ")
s2=input("please enter the 2nd line: ")
s3=input("please enter the 3rd line: ")

fmt="%%%ds" % max(len(s1),len(s2),len(s3))  #example: %%%ds=%%9s='         %s'
print('fmt= ', fmt)
print(fmt %s1)
print(fmt %s2)
print(fmt %s3)