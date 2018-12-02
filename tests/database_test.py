import sqlite3

conn = sqlite3.connect('../database/db.sqlite3')
c = conn.cursor()

c.execute('''SELECT * FROM anime WHERE score >= 8.5;''')
for item in c.fetchall():
	print(item[2])

conn.close()
