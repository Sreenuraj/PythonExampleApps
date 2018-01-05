import sqlite3

# function which will connect and create the table book
def connect():
    conn = sqlite3.connect('BookStore.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id integer primary key, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

#function which inserts the rows
def insert(title, author, year, isbn):
    conn = sqlite3.connect('BookStore.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(null,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

#function to get all data
def view():
    conn = sqlite3.connect('BookStore.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

# Search function
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('BookStore.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# function to delete a row based on id
def delete(id):
    conn = sqlite3.connect('BookStore.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

# function to update a row
def update(id, title, author, year, isbn):
    conn = sqlite3.connect('BookStore.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id=?",(title, author, year, isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("Sreenu's book 1",'Sreenuraj',2018,772211)
#print(view())
#print(search(year=2018))
#delete(2)
#update(2,'sreenu-book','sreenu',2017,999888)
#print(view())
