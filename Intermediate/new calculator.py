'''
This program is made for advance calculations like sum, subtraction, multiplication, division, squre, cube..

This code is written by vivek devkar.

Don't copy
learn from this code..

'''

# define function for further calculations


def sum(x,y):
	return x+y
	
def subtraction (x,y):
	return x-y
	
def multiplication(x,y):
	return x*y
	
def division(x,y):
	return x/y
	
def squre(x):
	return x**2
	
def cube(x):
	return x**3
	
def squreroot(x):
	return x**0.5
	
def cuberoot(x):
	return x**0.3333


# use while loop for continuous calculatin..

	
while True:
	print("entre your choice -->")
	print("1 - addition")
	print("2 - subtraction")
	print("3 - multiplication")
	print("4 - division")
	print("5 - squre")
	print("6 - cube")
	print("7 - squre root")
	print("8 - cube root")
	print("9 - average")
	print("10 - sin")
	print("11 - cos")
	print("12 - tan")
	print("0 - quit")
	
	choice=float(input("entre your choice -->"))
	
	if choice==0:
		break

# to break loop after some time..
# above Syntex is written for calculations..
		
	elif choice<5:
		num1 = float(input("entre 1st number -->"))
		num2 = float(input("entre 2nd number -->"))
		if choice==1:
			print(sum(num1,num2))
			
		
		elif choice==2:
			print (subtraction (num1,num2))
			
		
		elif choice==3:
			print(multiplication (num1,num2))
			
		
		elif choice==4:
			print(division (num1,num2))
			
	
	if choice==5:
		num=float(input("entre a number -->"))
		print(squre(num))
			
	elif choice==6:
		num=float(input("entre a number --> "))	
		print(cube(num))
		
	elif choice == 7:
			num=float(input("entre a number -->"))
			print(squreroot(num))
			
	elif choice==8:
			num=float(input("entre a number -->"))
			print(cuberoot(num))
			
	
	if choice==9:
		len=int(input("how many number you want to calculate -->"))
		total=0
		for i in range (1,len+1):
			element=float(input("entre  numbers -->"))
			total=total+element
			ave=total/i
		average=float(ave)
		print("average is",average)
		
	if choice == 10:
		num = float(input("entre a angle in degree (°) --> "))
		from math import sin
		print(sin(num))
		
	elif choice == 11:
		num = float(input("entre a angle in degree (°) --> "))
		from math import cos
		print(cos(num))
		
	elif choice==12:
		num = float(input("entre a angle in degree (°) --> "))
		from math import tan
		print(tan(num))
		
	else:
		print("entre correct option")
