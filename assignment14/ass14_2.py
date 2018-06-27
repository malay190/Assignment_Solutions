#Q.2- Write a Python program to count the frequency of words in a file.

f=open("test.txt","r")
content=f.read()
words=content.split()

uniwords=set(words)
for word in uniwords:
	print(word, words.count(word))

