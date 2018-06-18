#Q.3- Print multiplication table of 12 using recursion.

def rec(x,y):
	if y<=10:
		t=x*y
		print(t)
		y+=1
		rec(x,y)

rec(12,1)
	 
	
		