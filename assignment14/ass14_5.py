#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and 
#then store it to another file.
import os
import random
list2=[]
n=int(input('How many random numbers:'))
os.remove("random.txt")
with open("random.txt","w") as afile:	
	for i in range(n):	#insert n random number as per user
		list2.append(random.randint(1, 100))
	#print(list2,"#")
	for x in range(len(list2)):		#write numbers in file
		afile.write(str(list2[x])+"\n")		#"\n"-print number line by line
	#afile.seek(0)
with open("random.txt","r+") as f1:
	list1=f1.readlines()
	for i in range(len(list1)):
		list1[i]=int(list1[i])	#type casting
	list1.sort()	#sorting
	#print(list1)
with open("random_sorted.txt","w") as f2:
	for x in list1:
		f2.write(str(x)+"\n")
		
