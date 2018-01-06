from tkinter import *
from backend import Database

database = Database('BookStore.db')

# function for the list_selected_row
def list_selected_row(event): # event comes with the binding
    try: #inside a try since if user clicks on empty list it throw IndexError
        global selected_row # creating a global variable so that we can access it from anywhere
        index = list1.curselection()[0] #curselection method for getting the selected row's index as tuple
        selected_row = list1.get(index) #with the index get the ID of the
        #print(selected_row)
        clear_entry()
        e1.insert(END,selected_row[1])
        e2.insert(END,selected_row[2])
        e3.insert(END,selected_row[3])
        e4.insert(END,selected_row[4])
    except IndexError:
        pass

# function for itrating through the db and displaying the result in the list box
def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

# function for the search buttons
def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

# function to insert entry to the db
def insert_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    clear_entry()
    view_command()

# function to update an entry in DB
def update_command():
    database.update(selected_row[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    clear_entry()
    view_command()

# function to delete a row
def delete_command():
    database.delete(selected_row[0])
    clear_entry()
    view_command()

# Function which clears the entry in text box which we can use in many other function
def clear_entry():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)


# Create a thinker object
window=Tk()
window.wm_title("BookStore")


#Create all the labels, entry, listbox,Scrollbar and buttons
#Labels
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#Entry box
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)
year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#Listbox
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
#Scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# Configure the scrollbar and Listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# To bind the selected list elements, where list_selected_row is a function we define.
list1.bind("<<ListboxSelect>>", list_selected_row)

#Buttons
b1=Button(window,text="View all", width=12, command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="Search entry", width=12, command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text="Insert entry", width=12, command=insert_command)
b3.grid(row=4,column=3)
b4=Button(window,text="Update selected", width=12, command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete selected", width=12, command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)

view_command() # so that the window loads with the db values if it has any
window.mainloop()
