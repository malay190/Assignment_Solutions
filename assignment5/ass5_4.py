#Que.Q.4- Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points(your input). points can only take on positive integer values up to 200. 
#If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Sorry! No prize this time."

num=int(input("enter a number between 1 to 200:"))
if num>1 and num<51:
	print("Sorry! No prize this time.")
elif num>50 and num<151:
	print("Congratulations! You won a [wooden dog]!")
elif num>150 and num<181:
	print("Congratulations! You won a [books]!")
elif num>180 and num<201:
	print("Congratulations! You won a [chocolates]!")
else:
	print("please enter a number between 1 to 200")
	
