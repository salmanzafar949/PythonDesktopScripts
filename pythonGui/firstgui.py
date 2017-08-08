from tkinter import *
root = Tk() #tkinter class Creates the blank window
# TheLable = Label(root, text="This is to easy")
# TheLable.pack()
topframe = Frame(root)
topframe.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topframe, text="Click me", fg="red")
button2 = Button(topframe, text="Click mee", fg="green")
button3 = Button(topframe, text="Click meee", fg="black")
button4 = Button(bottomFrame, text="Click meeee", fg="blue")

button1.pack(side=LEFT)
button2 .pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()