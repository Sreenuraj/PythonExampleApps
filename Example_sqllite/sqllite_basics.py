import sqlite3

def create_db_cur():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    return(con,cur)

def create_table(con,cur,table_name):
    cur.execute("CREATE TABLE IF NOT EXISTS "+ table_name+"(Id Int, Item Text, Value Real)")
    con.commit
    return table_name

def table_insert(con,cur,table_name,id,item,value):
    cur.execute("INSERT INTO "+table_name+" VALUES(?,?,?)",(id,item,value))
    con.commit

def table_select(con,cur,table_name):
    row = cur.execute("SELECT * FROM "+table_name)
    print(row.fetchall())

def connection_close(con,cur):
    con.close()

(con,cur) = create_db_cur()
table_name = create_table(con,cur,'shop')
table_insert(con,cur,table_name,1,'bread',23.5)
table_insert(con,cur,table_name,2,'butter',20.5)
table_insert(con,cur,table_name,3,'jam',28.5)
table_select(con,cur,table_name)
connection_close(con,cur)
