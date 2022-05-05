n=int(input("enter the year"))
if(n%4==0):
	if(n%100==0):
		if(n%400==0):
			print("It is leap year")  
else:
	print("It is not leap year")
