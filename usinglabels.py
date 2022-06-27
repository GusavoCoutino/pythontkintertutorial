from tkinter import *

root = Tk()
label = Label(root, text='Hello Python')
#label['text'] = "Hello TKinter"
label.config(text="Hello TKinter", fg="red")
label.config(bg="yellow")
label.config(font="Times 15")
label.config(text="Hello Python Goodbye Python Hello")
label.config(wraplength="150")
label.config(justify=RIGHT)
label.pack()
root.geometry("300x250")
root.mainloop()