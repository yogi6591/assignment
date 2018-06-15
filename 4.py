#create a list with user defined data.
x=int(input("enter 0th element of list of integer type"))
y=int(input("enter 1st element of list of integer type"))
z=float(input("enter the 2nd element of list of float type"))
m=str(input("enter the 3rd element of list of any type"))
n=str(input("enter the 4th element of list of any type"))
p=(input("enter the 5th element of list of any type"))
T=(x,y,z,m,n,p)
print(T)
print("length of list=",len(T))
print("\n**********************\n")

#find largest and smallest element in tuple.
n=int(input("enter the total number of elements you want to insert in tuple"))
i=0
t1=[]
for i in range(0,n,1):
	t1.append(int(input("enter the elements in tuple")))
	i+=1
t2=tuple(t1)
print(t2)
print("largest number in tuple",max(t1))
print("smallest number in tuple",min(t1))
print("\n**********************\n")


#wap to find the product of all elements of tuple.
t2=(2,3,4,5,6,2,3,5)
i=0
p=1
for i in t2:
	p=p*i
print(t2)
print("product of tuple elements",p)
print("\n**********************\n")


#creation of sets and perform the operations on it.
num1=int(input("enter the 1st element"))
num2=int(input("enter the 2nd element"))
num3=int(input("enter the 3rd element"))
num4=int(input("enter the 4th element"))
num5=int(input("enter the 5th element"))
num6=int(input("enter the 6th element"))
set1=set([num1,num2,num3,num4,num5,num6])
print(set1)
n1=int(input("enter the 1st element"))
n2=int(input("enter the 2nd element"))
n3=int(input("enter the 3rd element"))
n4=int(input("enter the 4th element"))
n5=int(input("enter the 5th element"))
n6=int(input("enter the 6th element"))
set2=set([n1,n2,n3,n4,n5,n6])
print(set2)
print("the difference between the sets\n",set1-set2)
print("compare these sets\n")
if set1==set2:
	print("sets are equal")
else:
	print("sets are not equal")
	
print("\n intersection of sets",set1 & set2)
print("\n**********************\n")


#create a dictionary to store name and marks of 10 students by user input.
dict={}
for i in range(1,11):
	x=input("enter name of student")
	dict[x]=int(input("enter the marks of student"))
	i+=1
print(dict)	
print("\n**********************\n")


#sort the dictionary created in previous question according to marks.
list1=list(dict)
list1.sort()
print(list1)
print("\n**********************\n")


'''
count the number of occurence of each letter in word "MISSISSIPPI".
store count of every letter with the letter in a dictionary.
 '''
list2=list("mississippi")
dict1={}
dict1['m']=list2.count('m')
dict1['i']=list2.count('i')
dict1['s']=list2.count('s')
dict1['p']=list2.count('p')
print("number of letter in word",dict1)

 


