import sqlite3
import main

con = sqlite3.connect("sql_2.db")
cur = con.cursor()
us_id = main.message.chat.id

cur.execute("CREATE TABLE IF NOT EXISTS consumers(name, poop INTEGER)")
cur.execute('''INSERT INTO consumers (name) VALUES (?),(us_id)''')


con.commit()





















