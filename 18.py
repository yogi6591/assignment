#GUI-2.


#Que-1.

print("Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.\n")

import tkinter
from tkinter import *

root=Tk()

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
dict={"yogi":1239283912,"ajay":9302939203,"amit":1029384756,"aman":1938472630,"yogesh":9384761023,"akshay":1726384905,"monu":4938403840}
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in dict:
    mylist.insert(END,i)
mylist.pack(fill=BOTH)
Scrollbar(mylist,orient="vertical")
scrollbar.config(command=mylist.yview)

#OR

#scrollbar['command']=mylist.yview
root.geometry("100x100")
root.minsize(50,50)
root.maxsize(250,250)
root.mainloop()





#Que-2.

print("In the same tkinter file as created above, create a function to insert items into the dictionary.\n")

#Here i'm using pack() so everything will look in the same way as defined in the sequence.
#it means firstly dictionary keys will be there and then entry column.
#so if we want to alter the positions of anything use grid() and place().


import tkinter
from tkinter import *

root=Tk()

def show():
    a=entry.get()
    b=entry1.get()
    mylist.insert(END,a)
    dict[a]=b
    print(dict)

name=False
Mobile=False

def name(event):
    entry.delete(0,END)
    name=True

def Mobile(event):
    entry1.delete(0,END)
    Mobile=True

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
dict={"yogi":1239283912,"ajay":9302939203,"amit":1029384756,"aman":1938472630,"yogesh":9384761023,"akshay":1726384905,"monu":4938403840}
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in dict:
    mylist.insert(END,i)
mylist.pack(fill=BOTH)


entry=Entry(root)
entry.insert(0,'name')
entry.bind("<Button>",name)
entry.pack()

entry1=Entry(root)
entry1.insert(0,'Mobile No.')
entry1.bind("<Button>",Mobile)
entry1.pack()


b=Button(root,text='Submit',command=show)
b.pack()

Scrollbar(mylist,orient="vertical")
scrollbar.config(command=mylist.yview)

#OR

#scrollbar['command']=mylist.yview
root.geometry("100x100")
root.minsize(50,50)
root.maxsize(250,250)
root.mainloop()
