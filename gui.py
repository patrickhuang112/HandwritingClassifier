from tkinter import *

root  = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


one = Label(root, text = 'One', bg = 'red', fg = 'white')
one.pack(fill = X	)

button1 = Button(topFrame, text = 'Button 1', fg = 'red')
button2 = Button(topFrame, text = 'Button 2', fg = 'red')
button3 = Button(topFrame, text = 'Button 3', fg = 'red')
button4 = Button(bottomFrame, text = 'Button 4', fg = 'blue')

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = RIGHT)


theLabel = Label(root, text = 'Hello')
theLabel.pack()
root.mainloop()