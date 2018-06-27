#FILE HANDLING

import os

#Que-1.
print("Write a Python program to read last n line of a file\n")

nol=0 #number of lines
a=0
n=int(input("\nEnter the number of lines that you want to print"))
f=open("text.txt",'r',encoding='utf8')
c=f.readlines()
for i in c:
     nol=nol+1
nol=nol-n
for i in c:
    a+=1
    if a>nol:
        print(i)
f.close()
print("\n***********************\n")



#Que-2.
f=open("text.txt", 'r', encoding="utf8").read().split()
s=sorted(set(f))
for word in s:
    print(f.count(word), word)
f.close()

print("\n***********************\n")

#Que-3.
print("\nWrite a Python program to copy the contents of a file to another file\n")
with open("text.txt",'r',encoding="utf8") as f3:
    with open("new.txt",'w',encoding="utf8") as f4:
        for i in f3:
            f4.write(i)

print("\n***********************\n")



# #Que-4.
print("Write a Python program to combine each line from first file with the corresponding line in second file\n")
f5=open("text.txt",'r',encoding="utf8").readlines()
f6=open("new.txt",'r',encoding="utf8").readlines()
a=0
for i in f5:
    print(f5[a]+f6[a])
    a=a+1

print("\n***********************\n")



#Que-5.
print("Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.\n")
import random
f7=open("number.txt",'w')
for i in range(10):
    num=random.randint(1,100)
    f7.write(str(num))
    f7.write("\n")
f7.close()

f7=open("number.txt",'r')
l = f7.readlines()
l.sort()

f7.close()

f8=open("sort.txt",'w')

for i in l:
    f8.write(i)
    f8.write("\n")

print(f8)
f8.close()






