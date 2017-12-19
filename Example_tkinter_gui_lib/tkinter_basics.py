from tkinter import *

# Intializing a window object
my_window = Tk()

def km_to_miles():
    print('hi')
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

# creating a button
b1 = Button(my_window, text='Enter', command= km_to_miles)
b1.grid(row=0,column=0)

#Entry box
e1_value = StringVar()
e1 = Entry(my_window, textvariable=e1_value)
e1.grid(row=0,column=1)

#Text box
t1 = Text(my_window, height=1, width=20)
t1.grid(row=0,column=3)

my_window.mainloop()
