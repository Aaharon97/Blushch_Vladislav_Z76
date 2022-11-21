import sqlite3


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO unames (username, password, registration_date) VALUES (?, ?, ?)", ('Name1', 22222222, 2000-5-15))
cur.execute("INSERT INTO unames (username, password, registration_date) VALUES (?, ?, ?)", ('Name2', 33333333, 2003-8-10))
connection.commit()
connection.close()