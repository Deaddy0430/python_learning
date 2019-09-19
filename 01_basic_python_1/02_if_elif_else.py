season=int(input("please enter a season from 1~4 "))

if(season==1):
	print("Spring is from month", (season-1)*4, "to month", season*3)
elif(season==2):
	print("Summer is from month", (season-1)*4, "to month", season*3)
elif(season==3):
	print("Autumn is from month", (season-1)*4, "to month", season*3)
elif(season==4):
	print("Winter is from month", (season-1)*4, "to month", season*3)
else:
	print("error season input")

month=int(input("please enter a month from 1~12 "))
if(1<=month<=3):
	print("Spring")
elif(4<=month<=6):
	print("Summer")
elif(7<=month<=9):
	print("Autumn")
elif(10<=month<=12):
	print("Winter")
else:
	print("error month input")