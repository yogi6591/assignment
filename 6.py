#Take 10 integer from user and print them on screen.
print("Take 10 integer from user and print them on screen.\n")
print("enter the 10 integer values ")
list1=[]
i=0
for i in range(1,11):
	list1.append(int(input("enter the element of list=")))
	i+=1
for i in range(0,10):
	print(list1[i])
print("\n************************\n")


#create a list of integers and make a new list having square of elements of previous list.
print("#create a list of integers and make a new list having square of elements of previous list.\n")
list2=[]
list3=[]
for i in range(1,6):
	list2.append(int(input("enter the element of list=")))
print("list having square of elements of previous list")
for i in range(0,len(list2)):
	list3.append(list2[i]*list2[i])
print(list3)
print("\n************************\n")


#Form a list containing integer,floats,strings make three lists to store them separately.
print("Form a list containing integer,floats,strings make three lists to store them separately.\n")
list4=[1,2,5.6,8,4.3,'a',7,'c','x',2.8]
float1=[]
int1=[]
string1=[]
for i in list4:
	if type(i)==type(1):
		int1.append(i)
	elif type(i)==type(2.1):
		float1.append(i)
	else:
		string1.append(i)
print("the list of integers\n",int1)
print("the list of float values\n",float1)
print("the list of string values\n",string1)



#Using range[1,101] make a list containing even and odd numbers.
print("Using range[1,101] make a list containing even and odd numbers.\n")
list7=[]
list8=[]
for i in range(1,101):
	if i%2==0:
		list7.append(i)
	else:
		list8.append(i)
print("list having even numbers")
print(list7)
print("list having odd  numbers")
print(list8)
print("\n************************\n")


#Print the given pattern.
print("Print the given pattern.\n")
for i in range(1,5):
	for j in range(1,i+1):	
	    print("*",end="")
	print()
print("\n************************\n")



#Craete a user defined dictionary and get keys corresponding to the value using for loop.
print("Craete a user defined dictionary and get keys corresponding to the value using for loop.\n")
dict={}
list9=[]
for i in range(1,6):
	x=input("enter key=")
	dict[x]=input("enter value=")
print(dict)	
for i in dict:
	list9.append(i)
print("\nkeys corresponding to the every value")
print(list9)
'''
#make above for-loop as a comment and execute the for-loop written below then the output will be something different.
for i in dict:
	print(i)
'''
print("\n************************\n")



#Perform input,search and deletion from a user list.
print("Perform input,search and deletion from a user list.")
list10=[]
count=0
flag=0
for i in range(1,11):
	list10.append(int(input("enter the element=")))
print(list10)
x=int(input("enter the element you want to delete="))
for i in range(1,11):
	if x in list10:
		list10.remove(x)
		count+=1
		flag+=1
if count==0:
	print("this element is not present in list")
else:
	print("this element is present",flag,"times in list")
print("list after operation",list10)
print("\n************************\n")


#Write an infinite loop.
a=input("please press something for seeing infinite loop")
print("Write an infinite loop.\n")
print("here i'll demonstrate infinite loop")
x=0
while x<2:
	print("infinite loop")

	