s=input("please enter a string: ")
print("the number of the space you entered is: ", s.count(" "))

s2=s.strip()
print("the number of valid characters you entered is: ", len(s2))

if s2.isdigit():
	print("the type you entered is number")