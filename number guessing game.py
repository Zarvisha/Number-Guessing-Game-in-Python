import random
import math
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import font
from tkinter import *
def f1(x):
    s1=t1.get()
    s2=t2.get()
    x=int(s1)
    y=int(s2)
    global a
    a=random.randint(x,y)
    global b 
    b=math.floor(math.log2(y-x+1))
    w1=tk.Tk()
    w1.geometry("800x400")
    w1.configure(bg="darkslategrey")
    label_font = font.Font(size=24)
    myFont = font.Font(size=12,weight="bold")
    custom_font = font.Font(size=20)

    l3=tk.Label(w1,text="You have only ",bg="darkslategrey",fg="white",
            font="label_font")
    l3.grid(row=2,column =0,padx=40,pady=60)
    p=math.floor(math.log2(y-x+1))
    l4=tk.Label(w1,text=p,bg="darkslategrey",fg="white",
            font="label_font")
    l4.grid(row=2,column =1,padx=40,pady=60)
    
    l6=tk.Label(w1,text="chances to guess the number",bg="darkslategrey",fg="white",
            font="label_font")
    l6.grid(row=2,column =2,padx=40,pady=60)
    l5=tk.Label(w1,text="Guess a number",bg="darkslategrey",fg="white",
            font="label_font")
    l5.grid(row=3,column =0,padx=40,pady=60)

    t3=tk.Entry(w1,width=10,font="custom_font")
    t3.grid(row=3,column=1)
    #t4=tk.Entry(w1,width=10,font="custom_font")
    #t4.grid(row=5,column=1)

    b2=tk.Button(w1,text="Guess!!")
    b2.grid(row=3,column=2,pady=20,padx=40,rowspan=2)
    b2.bind("<ButtonRelease-1>",f2)
    b2['font'] = myFont

def f2(y):
    s3=StringVar()
    global b
    p=int(s3)
    count=0
    while count<b :
        count+=1
        if p==a:
           mb.showinfo(title=None, message='Congrtas You guessed the number' )
           break
        elif p<a :
            mb.showinfo(title=None,message='You guessed too small')
        elif p>a :
            mb.showinfo(title=None,message='You guessed too high')
    if count>= b:
        info.messagebox(title=None, message='You lost the game..Better luck next time')
    
w=tk.Tk()
w.geometry("800x400")
w.configure(bg="darkslategrey")
label_font = font.Font(size=24)
myFont = font.Font(size=12,weight="bold")
custom_font = font.Font(size=20)
l1=tk.Label(text="Enter the lower bound :",fg="white",bg="darkslategrey",
            font="label_font")
l1.grid(row=0,column=0,padx=40,pady=20)
l2=tk.Label(text="Enter the upper bound :",bg="darkslategrey",fg="white",
            font="label_font")
l2.grid(row=1,column=0,padx=40,pady=20)
t1=tk.Entry(width=10,font="custom_font")
t1.grid(row=0,column=1)
t2=tk.Entry(width=10,font="custom_font")
t2.grid(row=1,column=1)
b1=tk.Button(text="Enter")
b1.grid(row=0,column=2,pady=20,padx=40,rowspan=2)
b1.bind("<ButtonRelease-1>",f1)
b1['font'] = myFont

w.mainloop()

