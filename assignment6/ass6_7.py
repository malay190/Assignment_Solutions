#Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.

d={}
for x in range(10):
	a = input("Enter a key: ")
	b = input("Enter a value: ")
	d[a]=b
print(d)	