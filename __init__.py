import sqlite3

connection = sqlite3.connect('db/nbookmark.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

try:
    cur = connection.cursor()
except sqlite3.Error as db_error:
    print(' '.join(db_error.args))

connection.commit()
connection.close()
