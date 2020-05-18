from tkinter import *
from sympy import*
from numpy import*
import math

a= Symbol('a')

def click(event):
   global scvalue
   text=event.widget.cget("text")
   print(text)

   if text == "=":
       if (scvalue.get().isdigit()):
           value = int(scvalue.get())
       else:
           value = eval(screen.get())

       scvalue.set(value)
       screen.update()

   elif text == "INT":

       value=scvalue.get()

       x=integrate(value,a)
       scvalue.set(x)

       screen.update()

   elif text == "C":
       scvalue.set("")
       screen.update()

   else:
       scvalue.set(scvalue.get()+ text)
       screen.update()

   if text == "a":
       p = scvalue.get()
       scvalue.set(p)

root=Tk()
root.geometry("644x600")
root.title('calculator')

scvalue=StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font='lucida 40 bold')
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f=Frame(root, bg="grey")
b=Button(f,text="9",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root, bg="grey")
b=Button(f,text="6",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root, bg="grey")
b=Button(f,text="3",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root, bg="grey")
b=Button(f,text="0",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root, bg="grey")
b=Button(f,text="INT",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="a",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click,tan)

b=Button(f,text="C",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root, bg="grey")
b=Button(f,text="-",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click,tan)

b=Button(f,text="^",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=5,pady=2,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()

