#Take a Input from user and check whether it is leap year or not.
print("Take a Input from user and check whether it is leap year or not.\n")
x=int(input("enter any year="))
if (x%4==0):
	print(x,"is a leap year")
else:
	print(x," is not a leap year")
print("\n******************\n")


#Take length and breadth input from user and check whether the dimensions are of square or rectangle. 
print("Take length and breadth input from user and check whether the dimensions are of square or rectangle.\n")
x=int(input("enter the length="))
y=int(input("enter the breadth="))
if x==y:
	print("the dimensions are of a square")
else:
	print("the dimensions are of a rectangle")
print("\n******************\n")


#Take the input age of 3 people and determine oldest and youngest among them.
print("Take the input age of 3 people and determine oldest and youngest among them.\n")
print("please enter the different age for every person as this algorithm cann't solve the problem correctly if two or all the person have same age\n")
p1_age=int(input("enter the age of first person="))
p2_age=int(input("enter the age of second person="))
p3_age=int(input("enter the age of third person="))
if p1_age>p2_age:
	if p1_age>p3_age:
		print("first person is the oldest one")
		if p2_age>p3_age:
			print("third person is the youngest one")
		else:
			print("second person is the youngest one")
	else:
		print("third person is the oldest one")
		print("second person is the youngest one")
elif p2_age>p3_age:
	if p2_age>p1_age:
		print("second person is the oldest one")
		if p1_age>p3_age:
			print("third person is the youngest one")
		else:
			print("first person is the youngest one")
	else:
		print("first person is the oldest one")
		print("third person is the youngest one")
elif p1_age>p3_age:
	if p1_age>p2_age:
		print("first person is the oldest one")
	else:
		print("second person is the oldest one")
		print("third person is the youngest one")
else:										
	if p1_age>p2_age:
		print("third person is the oldest one")
		print("second person is the youngest one")
	else:
		print("third person is the oldest one")
		print("first person is the youngest one")
print("\n******************\n")


#Write an if statement to lets competitor know which of these prizes they won.
print("Write an if statement to lets competitor know which of these prizes they won.\n")
x=int(input("enter your earned points that must be <200  "))
if x>200:
	print("you have entered wrong points that is >200 ")
	'''
	print("please enter the points that must be <200")
	x=int(input("enter your points "))
	'''
elif x>=1  and x<=50:
	print("Sorry! no prize this time.")
	'''
	print("You can try again")
	print("if you want to play again enter 1 if donn't want then press 0")
	y=int(input("enter 0 or 1 to proceed  "))
	if y==0:
		print("Okey, so you have decided not to play again")
		print("Thanks for playing")
	else:
		x=int(input("enter your points<200  "))
	'''
elif x>=51 and x<=150:
		print("Congratulatios!, you won a Wooden Dog")
elif x>=151 and x<=180:
	print("Congratulatios!, you won a Book")
elif x>=181 and x<=200:
	print("Congratulatios!, you won Chocolates")
print("\n******************\n")

	

#Print total cost after getting discount.
print("Print total cost after getting discount.\n")
x=int(input("enter the number of units you want to buy="))
total_cost=x*100
print("total cost of your purchasing",total_cost)
if total_cost>1000:
	discount=(total_cost*10)/100
	print("total cost of your purchasing after getting discount=",total_cost-discount)
else:
	print("total cost of your purchasing without any discount as your total cost is not >1000=",total_cost)
	
	
	