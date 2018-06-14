#Que.Take the input age of 3 people and determine oldest and youngest among them.
a=int(input("enter the age of first person:"))
b=int(input("enter the age of second person:"))
c=int(input("enter the age of third person:"))
if a>b:
	if b>c:
		print("first person is the elder",a)
		print("third person is the younger",c)
	else :
		print("third person is the elder",c)
		print("second person is the younger",b)
else:
	if a>c:
		print("second person is the elder",b)
		print("third person id the younger",c)
	else:
		print("third person is the elder",c)
		print("first person id the younger",a)
		
		