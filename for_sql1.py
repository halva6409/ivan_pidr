import sqlite3,telebot
import main
def ddb():
    conn = sqlite3.connect("sql_1.db") 
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS classesssw(number, name, time)")



    conn.commit()
