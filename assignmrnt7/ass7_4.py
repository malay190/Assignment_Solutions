#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
count=0
def power(a,b):
	if b==1:
		return a
	else:
		p=a*power(a,b-1)
		return p
a=int(input("please enter base:"))
b=int(input("please index of base:"))
print(power(a,b))
		
		