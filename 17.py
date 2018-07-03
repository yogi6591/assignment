import tkinter
import sys
from tkinter import *


#Background color

#<widget>.configure(bg="color") here widget is any object
#For Ex
#root.configure(bg="red")


#OR

#root["bg"]="black"


# #Que-1.

root =Tk()

print("Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.\n")

def Hello_World():
    lable=Label(root,text="Hello World")
    lable.pack()


#without function print hello world on interface using lable
# lable = Label(root, text="Hello World")
# lable.pack()

Hello_World()
root.geometry("150x150")
root.minsize(100,100)
root.maxsize(200,200)
button=Button(root,text="Exit",bg="red",fg="black",height="1",width='3',command="exit") #Here exit is a function of sys module that can also be used as sys.exit()
button.pack()
root.mainloop()



#Que-2.

root1=Tk()

print("Write a python program to in the same interface as above and create a action when the button is click it will display some text.\n")


lable=Label(root1,text="Please click on more button given below")
lable.pack()

def action():
    lable.config(text="you have clicked the more button")
    lable.place(x="150",y="40")


root1.geometry("450x450")
root1.minsize(300,300)
root1.maxsize(500,500)
button=Button(root1,text="More",bg="red",fg="black",height="1",width='3',command=action)
button.pack()
root1.mainloop()



#Que-3.

print("Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.\n")

root2=Tk()

f1=Frame(root2)
f1.pack()

#Frame color
f1.configure(bg="green")


lable=Label(f1,text="it's a lable in frame f1")
lable.pack()

def show():
    lable.config(text="It's new text")
    lable.pack()
button1=Button(f1,text="Exit",command=exit,bg="skyblue")
button1.pack()

button2=Button(f1,text="Change the Lable Text",command=show,bg="skyblue")
button2.pack()

root2.geometry("350x350")
root2.minsize(100,100)
root2.maxsize(400,400)
root2.mainloop()



#Que-4.

print(" Write a python program using tkinter interface to take an input in the GUI program and print it.\n")

root3=Tk()

lable=Label(root3,text="Enter something in input box")
lable.pack()

def show():
    a=(entry.get())
    lable=Label(root3,text=a)
    lable.pack()

entry=Entry(root3,width="20")
entry.pack()
button=Button(root3,text="Click to print",command=show)
button.pack()
root3.geometry("350x350")
root3.minsize(100,100)
root3.maxsize(400,400)
root3.mainloop()