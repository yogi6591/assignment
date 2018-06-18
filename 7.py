
#Create a function to calculate  the area of a circle by taking radius from user.
print("Create a function to calculate  the area of a circle by taking radius from user.\n")
def area(radius):  #function definition
    ans=3.14*radius*radius
    print("area is=",ans)
a=int(input("enter the radius"))
area(a)  #function call
print("\n**************************\n")



#Write a function "perfect() that determines if parameter number is a perfect number.USe this function in a program that determines and prints all the perfect number between 1 and 1000.
print("Write a function perfect() that determines if parameter number is a perfect number.\n")
li=[]
def perfect():
    for n in range(1,1001):
        l=[]
        sum=0
        for x in range(1,n):
             if n%x==0:
                l.append(x)
        for i in l:
            sum=sum+i
        if sum==n:
            li.append(n)

perfect()
print("perfect number list is",li)
print("\n**************************\n")


#print multiplication table of 12 using recursion.
print("print multiplication table of 12 using recursion\n")
n=12
i=1
def table(n,i):
    if i>10:
        return
    else:
        print(n*i)
        table(n,i+1)
table(12,i)
print("\n**************************\n")


#Write a function to calculate power of a number raised to other (a^b) using recursion.
print("Write a function to calculate power of a number raised to other (a^b) using recursion.\n")
x=int(input("enter any number whose power you want to calculate"))
y=int(input("enter the number you want to use a power"))
def power(x,y):
    ans=1
    if y==1:
        return x
    else:
        ans=x*power(x,y-1)
        return ans
print(power(x,y))
print("\n**************************\n")


#Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
print("Write a function to find factorial of a number but also store the factorials calculated in a dictionary.\n")
x=int(input("enter the number whose factorial yon want to calculate"))
dict={}
def fact(a):
    if a==1 or a==0:
        return 1
    else:
        ans=a*fact(a-1)
        return ans
ans=fact(x)
dict[x]=ans
print(dict)
