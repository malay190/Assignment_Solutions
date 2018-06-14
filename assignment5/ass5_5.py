#Que.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
print("1unit=100")
unit=int(input("enter number of unit you want to buy:"))
price=unit*100

if price>1000:
	price=price-price/10
	print("total cost of purchasing:",price)
else:
	print("total cost of purchasing:",price)