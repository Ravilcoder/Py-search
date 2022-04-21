import sqlite3 as sl
import os


con = sl.connect('userdata.db')
cur = con.cursor()

#создание таблицы

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            telegram TEXT UNIQUE,
            interests TEXT NOT NULL
        );
    """)

sql = 'INSERT or REPLACE INTO users (id, name, age, gender, telegram, interests) values(?, ?, ?, ?, ?, ?)'

data = [
    (1, 'Alice', 21, 'Woman','@huy', 'FOOTBALL SPORT GAMES'),
    (2, 'Bob', 22, 'Man', '@govno', 'FOOTBALL SPORT GAMES' ),
    (3, 'Chris', 23, 'Man', '@pizda', 'FOOTBALL SPORT GAMES' )
]
with con:
    con.executemany(sql, data) # EXECUTE - ДОБАВЛЕНИЕ ДАННЫХ(1 пользователь)
    
'''cur.execute("SELECT * FROM users;")
three_results = cur.fetchmany(2)
print(three_results)'''
cur.execute("SELECT * FROM users;")
first_user = cur.fetchone(2)
print(first_user)

    