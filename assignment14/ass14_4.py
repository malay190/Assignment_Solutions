#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open("test.txt","r") as f1:
	content1=f1.readlines()
	n1=len(content1)

with open("abc.txt","r") as f2:
	content2=f2.readlines()
	n2=len(content2)
i=0
for x in range(min(n1,n2)):
	print(content1[i]+content2[i])
	i = i+ 1