from tkinter import *
from math import sqrt
root = Tk()
root.title("calX")

e= Entry(root, width=50, borderwidth=10, fg="white", bg="Black")
e.grid(row=0, column=0,columnspan=10,padx=10,pady=10)

def button_click(number):
    current=e.get()
    if number == "-" and not current:
        e.insert(0, "-")
    elif number != "-":
        e.delete(0,END)
        e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0,END)

def addition():
    first_number = e.get()
    global f_num
    global operation
    operation="Add"
    f_num = int(first_number)
    e.delete(0,END)

def subtraction():
    first_number = e.get()
    global f_num
    global operation
    operation="Sub"
    f_num = int(first_number)
    e.delete(0,END)

def multiplication():
    first_number = e.get()
    global f_num
    global operation
    operation="Mul"
    f_num = int(first_number)
    e.delete(0,END)

def division():
    first_number = e.get()
    global f_num
    global operation
    operation="Div"
    f_num = int(first_number)
    e.delete(0,END)

def square():
    first_number = e.get()
    global f_num
    global operation
    operation="Sq"
    f_num = int(first_number)
    e.delete(0,END)

def Sqrt():
    global operation
    operation="root"
    e.delete(0,END)

def equal(event=None):
    second_number = e.get()
    e.delete(0, END)
    if operation == "Add":
        e.insert(0, f_num + int(second_number))
    if operation == "Sub":
        e.insert(0, f_num - int(second_number))
    if operation == "Mul":
        e.insert(0, f_num * int(second_number))
    if operation == "Div":
        e.insert(0, f_num / int(second_number))
    if operation == "Sq":
        e.insert(0, f_num ** int(second_number))
    if operation == "root":
        e.insert(0,sqrt(float(second_number)))
root.bind('<Return>',equal)





button_0= Button(root,text="0",padx=30, pady=20,command=lambda:button_click(0),fg="white",bg="black")
button_1= Button(root,text="1", padx=30,pady=20,command=lambda:button_click(1),fg="white",bg="black")
button_2= Button(root,text="2", padx=30,pady=20,command=lambda:button_click(2),fg="white",bg="black")
button_3= Button(root,text="3", padx=30,pady=20,command=lambda:button_click(3),fg="white",bg="black")
button_4= Button(root,text="4", padx=30,pady=20,command=lambda:button_click(4),fg="white",bg="black")
button_5= Button(root,text="5", padx=30,pady=20,command=lambda:button_click(5),fg="white",bg="black")
button_6= Button(root,text="6", padx=30,pady=20,command=lambda:button_click(6),fg="white",bg="black")
button_7= Button(root,text="7", padx=30,pady=20,command=lambda:button_click(7),fg="white",bg="black")
button_8= Button(root,text="8", padx=30,pady=20,command=lambda:button_click(8),fg="white",bg="black")
button_9= Button(root,text="9", padx=30,pady=20,command=lambda:button_click(9),fg="white",bg="black")
button_a= Button(root,text="+", padx=30,pady=20,command=addition,fg="white",bg="black")
button_s= Button(root,text="-", padx=30,pady=20,command=subtraction,fg="white",bg="black")
button_m= Button(root,text="*", padx=30,pady=20,command=multiplication,fg="white",bg="black")
button_d= Button(root,text="/", padx=30,pady=20,command=division,fg="white",bg="black")
button_rt= Button(root,text="√", padx=30,pady=20,command=Sqrt,fg="white",bg="black")
button_sq= Button(root,text="^", padx=30,pady=20,command=square,fg="white",bg="black")
button_clr= Button(root, text="Clear", padx=60, pady=20,command=button_clear,fg="white",bg="black")
button_eq= Button(root, text="=",padx=30,pady=50,command=equal,fg="white",bg="black")

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_a.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_s.grid(row=2,column=3)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_m.grid(row=3,column=3)
button_sq.grid(row=5,column=3)
button_0.grid(row=4,column=1)
button_rt.grid(row=4,column=2)
button_d.grid(row=4,column=3)
button_clr.grid(row=5,column=1,columnspan=2)
button_eq.grid(row=4,rowspan=2,column=0)



root.mainloop()
