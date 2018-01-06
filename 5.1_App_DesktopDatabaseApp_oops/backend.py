import sqlite3

class Database:

    # init function to initialize the Database
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id integer primary key, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    #function which inserts the rows
    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(null,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()

    #function to get all data
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    # Search function
    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    # function to delete a row based on id
    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    # function to update a row
    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id=?",(title, author, year, isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
