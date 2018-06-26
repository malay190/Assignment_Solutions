#Q.2- Name and handle the exception occurred in the following program: 

# l=[1,2,3]
# print(l[3])

# improved code

l=[1,2,3]
try:
	print(l[3])
except Exception as e:
	print(e)	#print exception name