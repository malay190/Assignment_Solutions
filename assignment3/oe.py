l=[1,2,4,7,5,6,8,9,12,13,15,17]
m=0
n=0
for x in l:

	if(x%2==0):
		m+=1
	else:
		n=n+1

print("total even number",m)
print("total odd number",n)

