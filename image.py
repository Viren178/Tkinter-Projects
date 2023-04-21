from tkinter import * 
from PIL import ImageTk,Image
root=Tk()
root.title("images&icons")
root.iconbitmap(r"C:\Users\A\Pictures\New folder\WhatsApp Image 2023-02-17 at 12.04.09.jpg")

my_img = ImageTk.PhotoImage(Image.open(""))

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()



root.mainloop()