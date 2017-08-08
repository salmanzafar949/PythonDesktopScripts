from tkinter import *

root = Tk()
theLable = Label(root, text="Responsive Layout", fg="Blue", bg="white")
theLable.pack()
one = Label(root, text="one", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="three", bg="blue", fg="pink")
three.pack(side=LEFT, fill=Y)
root.mainloop()