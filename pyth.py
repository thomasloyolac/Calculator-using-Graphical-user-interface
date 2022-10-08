import math
from tkinter import *

root=Tk()
e=Entry(root,borderwidth=4,fg='blue',width=35)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def button_click(number):
    curr=e.get()
    e.delete(0,END)
    e.insert(0, str(curr) + str(number))


def button_clear():
    e.delete(0,END)


def button_add():
    first_number=e.get()
    e.delete(0,END)
    global f_num 
    global math
    math='addition'
    f_num=int(first_number)

def button_subtraction():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math='subtraction'
    f_num=int(first_number)

def button_multiplication():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math='multiplication'
    f_num=int(first_number)


def button_division():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math='division'
    f_num=int(first_number)



def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,int(f_num)+int(second_number))
    if math=='subtraction':
        e.insert(0,int(f_num) -int(second_number))
    if math=='multiplication':
        e.insert(0,int(f_num) *int(second_number))
    if math=='division':
        e.insert(0,int(f_num) /int(second_number))    
#def button_minus():

    

button_1=Button(root,text='1',padx=40,pady=20,command= lambda:button_click(1)).grid(row=3,column=1)
button_2=Button(root,text='2',padx=40,pady=20,command=lambda:button_click(2)).grid(row=3,column=2)
button_3=Button(root,text='3',padx=40,pady=20,command=lambda:button_click(3)).grid(row=3,column=3)
button_4=Button(root,text='4',padx=40,pady=20,command=lambda:button_click(4)).grid(row=2,column=1)
button_5=Button(root,text='5',padx=40,pady=20,command=lambda:button_click(5)).grid(row=2,column=2)
button_6=Button(root,text='6',padx=40,pady=20,command=lambda:button_click(6)).grid(row=2,column=3)
button_7=Button(root,text='7',padx=40,pady=20,command=lambda:button_click(7)).grid(row=1,column=1)
button_8=Button(root,text='8',padx=40,pady=20,command=lambda:button_click(8)).grid(row=1,column=2)
button_9=Button(root,text='9',padx=40,pady=20,command=lambda:button_click(9)).grid(row=1,column=3)
button_0=Button(root,text='0',padx=40,pady=20,command=lambda:button_click(0)).grid(row=4,column=1)
button_add1=Button(root,text='+',padx=40,pady=30,command=button_add).grid(row=5,column=1)
button_clear1=Button(root,text='Clear',padx=85,pady=30,command=button_clear).grid(row=6,column=2,columnspan=2)
button_equal1=Button(root,text='=',padx=95,pady=30,command=button_equal).grid(row=5,column=2,columnspan=2)
button_minus1=Button(root,text='-',padx=40,pady=20,command=button_subtraction).grid(row=6,column=1)
button_multiply=Button(root,text='x',padx=40,pady=20,command=button_multiplication).grid(row=4,column=2)
button_divide=Button(root,text='/',padx=40,pady=20,command=button_division).grid(row=4,column=3)


root.mainloop()





