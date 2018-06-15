#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

l=[]
for x in range(5):
	l.append(int(input("enter the number:")))
print(l)

l1=[]
for x in range(5):
	l1.append(l[x]**2)
print(l1)
	