s=input("please enter a string: ")
s2=s[1:-1]	#from s[1] to s[-1]
print("the sting after process is:", s2)

s=input("please enter a string for checking mirror: ")
s3=s[::-1]	#every s[n-1], n start from 0
if s3==s:
	print(s, "is a mirror string")
else:
	print(s, "is not a mirror string")