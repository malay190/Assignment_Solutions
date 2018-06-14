#Que.Q.1- Take an input year from user and decide whether it is a leap year or not.
 
year=int(input("enter any year:"))
if year%4==0:
	if year%100==0:
		if year%400==0:
			print("entered number is a leap year")
		else :
			print("entered number is not a leap year")
	else :
		print("entered number is not a leap year")
else :
	print("entered number is not a leap year")
			
	 