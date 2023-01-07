import sqlite3

conn = sqlite3.connect('colegio.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM alumnos WHERE nombre="William"')
for row in rows:
    print(row)
cursor.close()
conn.close()