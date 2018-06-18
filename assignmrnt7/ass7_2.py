#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number.
	#Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 


def perfect(num):
	sum=0
	for x in range(1,num):
		if num%x==0:
			sum=sum+x
	if sum==num:
		print(num,":is a perfect number")
for x in range(1,1001):
	perfect(x)
	
