# THREADS


#Create a threading process such that it sleeps for 5 seconds and then prints out a message.
print("Create a threading process such that it sleeps for 5 seconds and then prints out a message.\n")
import threading
from threading import Thread
import time

def display():
    print("Wait for 5 seconds\n")
    time.sleep(5)
    print("It was slept for 5 seconds")

t1 = Thread(target=display)
t1.start()
t1.join()
print("\n***********************************\n")






#Make a thread that prints number from 1-10,waits for 1 sec between.
print("Make a thread that prints number from 1-10,waits for 1 sec between.\n")
import threading
from threading import Thread
import time
def display():
    for x in range(1,11):
        print(x)
        time.sleep(1)

t2=Thread(target=display)
t2.start()
t2.join()
print("\n***********************************\n")





'''
Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
Delay goes like 2sec-->4sec-->6sec-->...
'''
print("Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.\nDelay goes like 2sec-->4sec-->6sec-->...")
import threading
from threading import Thread
import time
def display(l):
    for x in l:
        print(x)
        time.sleep(1)

l=[2,34,6,9,12]
t3=Thread(target=display,args=(l,))
t3.start()
t3.join()
print("\n***********************************\n")





#Call factorial function using thread.
print("Call factorial using thread\n")
import threading
from threading import Thread
import time
import math
def factorial():
     fact=1
     for x in range(1,num+1):
         fact=fact*x
     print("Factorial of ",num,"is",fact)

num=int(input("Enter any  number"))
t4=Thread(target=factorial)
t4.start()