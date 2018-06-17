#create a list with user defined data.
print("create a list with user defined data.\n")
x=int(input("enter 0th element of list of integer type"))
y=int(input("enter 1st element of list of integer type"))
z=float(input("enter the 2nd element of list of float type"))
m=str(input("enter the 3rd element of list of any type"))
n=str(input("enter the 4th element of list of any type"))
p=(input("enter the 5th element of list of any type"))
list1=[x,y,z,m,n,p]
print(list1)
print("\n**********************\n")


#add a given list to above created list.
print("add a given list to above created list.\n")
list2=['google','apple','facebook','microsoft','tesla']
mergedlist=list1+list2
print("the mergedlist is\n",mergedlist)
print("\n**********************\n")
	
		
#count the number of time an object occurs in a list.
print("count the number of time an object occurs in a list.\n")
list=[1,2,3,2,3,'x',4,4,5,3,4,'x',4,5,7,9]
print(list)
print("how many time 1 occurs in above list=",list.count(1))
print("how many time 4 occurs in above list=",list.count(4))
print("how many times 8 occur in above list=",list.count(8))
print("how many time x occurs in above list=",list.count('x'))
print("how many times y occurs in above list=",list.count('y'))
print("\n**********************\n")


#create a list of numbers and sort them in ascending order.
print("create a list of numbers and sort them in ascending order.\n")
a=int(input("enter 0th element of list"))
b=int(input("enter 1st element of list"))
c=int(input("enter the 2nd element of list"))
d=int(input("enter the 3rd element of list"))
e=int(input("enter the 4th element of list"))
f=int(input("enter the 5th element of list"))
list3=[a,b,c,d,e,f]
print("the list is")
print(list3)
list3.sort()
print("the sorted list ")
print(list3)
print("\n**********************\n")


#Add two sorted lists A & B and the resulted list must be in ascending oredr.
print("Add two sorted lists A & B and the resulted list must be in ascending oredr.\n")
list4=[1,4,6,7,9,10,15]
list5=[0,2,3,6,8,13,18]
print(list4)
print(list5)
list6=list4+list5
list6.sort()
print("the resulted sorted list will be looked like ")
print(list6)
print("\n**********************\n")


#implement a stack and queue using lists.
print("implement a stack and queue using lists.\n")
list7=['ajay',115,295,'yogi']
print("\n operations of stack")
print("stack principle is 'last in-first out'\n")
print("here i'm adding two elements in list")
list7.append('amar')
list7.append(212)
print("now list will be like that\n",list7)
print("\n now i'm removing the elements from the list")
list7.pop()
list7.pop()
list7.pop()
print("after removing the elements from list\n",list7)
print("\n-*-*-*-*-*-*-*-*-")
print("\noperations of queue")
list8=[121,'ram','acadview',292]
print("\nqueue principle is first in-first out")
print("here i'm adding two elements in list")
list8.append(100)
list8.append('laptop')
print(list8)
list8.reverse()
print(list8)
print("now i'll pop the elements from the list")
list8.pop()
list8.pop()
print(list8)		
print("\n**********************\n")

#Question. count even and odd number in that list.
print("Question. count even and odd number in that list.\n")
list9=[2,7,3,6,9,3,8,18,37,49]
even=0
odd=0
for i in list9:
 if i%2==0:
  even+=1
 else:
  odd+=1
print("total even number in list",even)
print("total odd numbers in list",odd)




