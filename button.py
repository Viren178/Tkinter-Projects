from tkinter import *
root = Tk()

def abtodekh():
    mylable=Label(root, text="rehne de bhai")
    mylable.pack()

mybutton = Button(root, text="idhar!", command=abtodekh, fg="white", bg="black")
mybutton.pack()

root.mainloop() 