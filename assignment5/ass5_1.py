#Que.Q.1- Take an input year from user and decide whether it is a leap year or not.
#method-1

year=int(input("enter any year:"))
if year%4==0:
	if year%100==0:
		if year%400==0:
			print("entered number is a leap year",1
		else :
			print("entered number is not a leap year",)
else :
	print("entered number is not a leap year",)
	
#method-2

year=int(input("enter any year:"))
if year%4==0:
	if year%100==0 and year%400==0:
		print("entered number is a leap year")
	else:
		print("entered number is not a leap year")
else:
	print("entered number is not a leap year")


		