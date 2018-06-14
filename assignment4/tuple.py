#Q.1- Create two set using user defined values. 

#Que. Calculate difference between two sets.

a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
d=int(input("enter any number"))
s1=set([a,b,c,d])
print(s1)

p=int(input("enter any number"))
q=int(input("enter any number"))
r=int(input("enter any number"))
s=int(input("enter any number"))
s2=set([p,q,r,s])
print(s2)
print("difference between two sets:",s1-s2)


#Que.  Print the result of intersection of two sets.

a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
d=int(input("enter any number"))
s1=set([a,b,c,d])
print(s1)

p=int(input("enter any number"))
q=int(input("enter any number"))
r=int(input("enter any number"))
s=int(input("enter any number"))
s2=set([p,q,r,s])
print(s2)
print("difference between two sets:",s1&s2)