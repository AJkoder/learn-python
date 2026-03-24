#SQLite
import sqlite3
conn=sqlite3.connect("students.db")
cursor=conn.cursor()
cursor.execute('''
            create table if not exists students(
                id integer primary key AUTOINCREMENT,
                name text,
                age INT)
                ''')
cursor.execute("INSERt INTO STUDENTS(NAME,AGE) VALUES('AJ',20)")
conn.commit()
cursor.execute("SELECT * FROM STUDENTS")
data = cursor.fetchall() 

print("Record:")
print(data)
for row in data:
    print(row)
conn.close()