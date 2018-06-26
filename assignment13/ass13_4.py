#Q.4- What will be the output of the following code:

# Function which returns a/b

#improved code
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")	#paranthesis missing in previoos code
	else:
		print(c)	#paranthesis missing in previoos code

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)