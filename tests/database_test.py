import sqlite3

conn = sqlite3.connect('../database.db')
c = conn.cursor()

c.execute('''SELECT * FROM anime WHERE score >= 9.0;''')
for item in c.fetchall():
	print(item)

conn.close()
