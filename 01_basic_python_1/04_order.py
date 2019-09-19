s=input("please enter a string: ")
if s != '':
	print("the code of first element in string is: ", ord(s[0]))

ch=int(input("please enter the code from 0~65535: "))
if 0 <= ch <= 65535:
	print("the character of", ch, "is: ", chr(ch))