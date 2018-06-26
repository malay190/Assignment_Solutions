#Q.5- Write a program to show and handle following exceptions: 
# 1. Import Error
# 2. Value Error
# 3. Index Error

#import errror

try:
	from surinder import mota
except Exception as e:
	print("import error")
	print("...............")
	
#value error

try:
	s=int(input("enter your name:"))
except Exception as e:
	print("value error")
	print("...................")
	
#index error

l=[1,2,3]
try:
	print(l[3])
except Exception as e:
	print(e)
	print("index error")
	
	
