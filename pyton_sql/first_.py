import sqlite3
conn = sqlite3.connect('school.db')
cursor = conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   age INTEGER
               )
               ''')
conn.commit()

cursor.execute('INSERT INTO students(name, age) VALUES (?,?)',('anuj', 19)
               )
conn.commit()
