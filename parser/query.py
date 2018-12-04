import sqlite3
import os
import sys
import json


def dict_factory(cursor, row):
	data = {}
	for index, col in enumerate(cursor.description):
		data[col[0]] = row[index]
	return data


path = os.path.dirname(os.path.abspath(__file__)) + "/db.sqlite3"
conn = sqlite3.connect(path)
conn.row_factory = dict_factory
c = conn.cursor()

if len(sys.argv) > 1:
	title = sys.argv[1]
	c.execute("SELECT * FROM anime WHERE title LIKE \'%{title}%\' ORDER BY rank ASC LIMIT 25".format(title=title))
else:
	c.execute('SELECT * FROM anime ORDER BY rank ASC LIMIT 25')

for entry in c.fetchall():
	print(json.dumps(entry))

sys.stdout.flush()
