#What is time tuple.
print("What is time tuple\n")
import datetime
import time
print("time tuple--\n",time.gmtime())
print("\n**************************\n")



#Write a program to get formatted time.
print("Write a program to get formatted time.\n")
import time
print("time structure--\n",time.localtime(time.time())) #time structure
print("\n")
print("formatted time--\n",time.asctime(time.localtime(time.time())))  #for formatted time
print("\n**************************\n")



#  Extract month from the time.
print("Extract month from the time.\n")
import datetime
from datetime import date
d=datetime.date.today()
print("month--",d.month)
print("\n**************************\n")



#Extract day from the time.
print("Extract day from the time.\n")
from datetime import datetime
a=datetime.now()
print("day--",a.strftime("%A"))
print("\n**************************\n")



#Extract date from the time.
print("Extract date from the time.\n")
import datetime
from datetime import date
d=datetime.date.today()
print("date--",d.day)
print("\n**************************\n")



#Write a program to print time using localtime.
print("Write a program to print time using localtime.\n")
import datetime
print("time using localtime--",time.asctime(time.localtime()))
print("\n**************************\n")



#Find the factorial of a number input by using math package functions.
print("\nFind the factorial of a number input by using math package functions.\n")
import math
x=int(input("enter any number whose factorial you want to calculate=="))
print("factorial is==",math.factorial(x))
print("\n**************************\n")



#Find the GCD of a number input by user using math package function.
print("Find the GCD of a number input by user using math package function.\n")
import math
x=int(input("enter any 1st number=="))
y=int(input("enter the 2nd number=="))
print("greatest common divisor--",math.gcd(x,y))
print("\n**************************\n")



#Use OS package and do the following tasks.
print("Use OS package and do the following tasks.\n")
print("1.Get current working directory.\n")
print("2.Get the user environment.\n")
import os
print("Current working directory--\n",os.getcwd())
print("\nUser environment--\n",os.environ)