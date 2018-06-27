#Q.1- Write a Python program to read last n lines of a file

n=int(input("enter the last n lines you want to read:"))
f=open('test.txt')
content=f.readlines()
while n>0:
	print(content[-n])
	n-=1
