from tkinter import *

root = Tk()

# thelabel = Label(root, text="Grid LayOut" ,bg="red")
# thelabel.pack(fill=X)
pwd  = Label(root, text="Name")
name = Label(root, text="Password")
e1 = Entry(root)
e2 = Entry(root)
pwd.grid(row=0, sticky=E)
name.grid(row=1, sticky=E)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me Logged In...!")
c.grid(columnspan=2)
root.mainloop()