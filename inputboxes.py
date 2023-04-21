from tkinter import *
root = Tk()

e= Entry(root,width=50, fg="green", bg="red", borderwidth=20)
e.pack()
e.get()
e.insert(0,"Tu hi bataega na bhai!")

def name():
    mylabel=Label(root, text="tu" + e.get())
    mylabel.pack()

mybutton=Button(root, text="tera naam bata",command=name)
mybutton.pack()
root.mainloop()