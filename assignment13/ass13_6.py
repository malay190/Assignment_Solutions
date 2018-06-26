#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
#The code must keep taking input till the user enters the appropriate age number(less than 18).

class AgeTooSmallError(Exception):	#user defined class created to form own exception
	pass
	
# def abc():
		# age=int(input("enter your age:")) 
		# if age<18:	#if age is less than 18 exception is raised
			# print("you are less than 18")
			# raise AgeTooSmallError("smaller")
		# else:
			# print("you are eligible!")

# try:		
	# abc()
# except AgeTooSmallError as e:
	# print(e)	#print name of exception
	# try:
		# abc()
	# except Exception:
		# print(e)
		# abc()
# else:
	# print("no exception found")
	
	
while True:
	try:
		x = int(input("Enter your age: "))
		if x < 18:
			raise AgeTooSmallError
		break
	except AgeTooSmallError:
		print("Age is too small")
		
print("You have entered correct age")
		