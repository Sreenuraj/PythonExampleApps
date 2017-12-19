from tkinter import *

window = Tk()

#converts the user input value to grams, pounds, and ounces
def convert():
    user_input = float(entry1_var.get())
    text1.insert(END, user_input*1000)
    text2.insert(END, user_input*2.20462)
    text3.insert(END, user_input*35.274)

label1 = Label(window, text="Kg")
label1.grid(row=0,column=0)

entry1_var = StringVar()
entry1 = Entry(window, textvariable=entry1_var)
entry1.grid(row=0,column=1)

button1 = Button(window, text='Convert', command=convert)
button1.grid(row=0,column=2)

text1 = Text(height=1,width=20)
text1.grid(row=1,column=0)
text2 = Text(height=1,width=20)
text2.grid(row=1,column=1)
text3 = Text(height=1,width=20)
text3.grid(row=1,column=2)


window.mainloop()
