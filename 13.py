#Exception Handling


#QUE-1.
print("Name and handle the exception occured in the following program:\n")
# a=3
# if a<4:
#     a=a/(a-3)
#     print(a)

#Name of Exception-->ZeroDivisonError
#Now i'll handle this exception by doing some changes.

a=3
try:
    if a<4:
        a=a/(a-3)
except Exception as e:
    print(e)

print("\n******************************\n")



#QUE-2.
print("Name and handle the exception occurred in the following program: \nl=[1,2,3]\nprint(l[3])\n\n")
#l=[1,2,3]
#print(l[3])

#Name of Exception-->IndexError
#Now i'll handle the program

l=[1,2,3]
try:
    print(l[3])
except Exception as e:
    print(e)

print("\n******************************\n")



#QUE-3.
print("What will be the output of the following code:\n")

#Program to depict Raising Exception

# try:
    # raise NameError("Hi there")  # Raise Error
# except NameError:
    # print("An exception")
    # raise  # To determine whether the exception was raised or not


# OUTPUT
# raise NameError("Hi there")  # Raise Error
# NameError: Hi there





#QUE-4.
print("What will be the output of the following code:")

# Function which returns a/b
# def AbyB(a , b):
	# try:
		# c = ((a+b) / (a-b))
	# except ZeroDivisionError:
		# print("a/b result in 0")
	# else:
		# print(c)

Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)



# OUTPUT
# -5.0
# a/b result in 0




#QUE-5.
print("Write a program to show and handle following exceptions: \n1. Import Error\n2. Value Error\n3. Index Error")

#Import Error

#import khushiram

#print("I tried to import an undefined module")


#Here i'll handle the exception raised above.

try:
    import khushiram
    print("I tried to import an undefined module")

except Exception:
    print("You have tried to import an undefined module")



#Value Error

#x=input("Enter any string")
#print(int(x))


#Here i'll handle the exception raised above.

try:
    x=input("Enter any string")
    print(int(x))
except Exception:
    print("You have tried to convert a string into an int--->>that raised--->>ValueError")



#Index Error


#l=[1,2,3,4,5]
#print(l[7])

try:
    l=[1,2,3,4,5]
    print(l[7])
except Exception:
    print("You have tried to access an index value that is not possible for the above list")

print("\n******************************\n")




#QUE-6.
print(" Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18).\n ")
class ValueTooSmallError(Exception):
      pass
while True:
   try:
      age=int(input("enter your age"))
      if age< 18:
        raise ValueTooSmallError("exception")
      else:
        print("You are eligible")
        break
   except ValueTooSmallError as e:
        print("this value is too samll ,try again!")
        print(e)



