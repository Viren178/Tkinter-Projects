from tkinter import *

root = Tk()

#creating a lable widget
mylable1 = Label(root, text="oooo helo!")
mylable2 = Label(root, text="sun le!")
# shoving it onto the screen
mylable1.grid(row=0,column=0)
mylable2.grid(row=1, column=2)

root.mainloop()

