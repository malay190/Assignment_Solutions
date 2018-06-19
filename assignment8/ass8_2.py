#Q.2- Write a program to get formatted time.

import time
format=time.asctime(time.localtime(time.time()))
print("formated time:",format)


#Q.3- Extract month from the time.

from datetime import datetime
p= datetime.now()
print(p)
print(p.strftime("%B"))


#Q.4- Extract day from the time.

from datetime import datetime
p= datetime.now()
print(p)
print(p.strftime("%A"))

#Q.5- Extract date (ex : 11 in 11/01/2021) from the time.

import datetime
p=datetime.date.today()
print(p)
print(p.day)

#Q.6- Write a program to print time using localtime method

import time
print(time.localtime())

#Q.7- Find the factorial of a number input by user using math package functions.

import math
a=math.factorial(int(input("enter any number:")))
print("factorial of that number:",a)


#Q.8- Find the GCD of a number input by user using math package functions.

import math
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("GCD:",math.gcd(a,b))

#Q.9- Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.

import os
print(os.getcwd())
print(os.environ)




