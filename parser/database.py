import sqlite3
import time
from jikan import Jikan

# establish database connection
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# create anime table
c.execute('''CREATE TABLE IF NOT EXISTS anime(
							id INTEGER PRIMARY KEY,
							rank INTEGER,
							title TEXT,
							image TEXT,
							type TEXT,
							episodes TEXT,
							start_date TEXT,
							end_date TEXT,
							score REAL);''')

jikan = Jikan()
MAX_PAGE = 100

# retrieve top 5000 anime
for page in range(1, MAX_PAGE + 1):
	response = jikan.top('anime', page, 'bypopularity')
	top = response['top']
	print(page, "/", MAX_PAGE)
	for item in top:
		values = (
			item['mal_id'],
			item['rank'],
			item['title'],
			item['image_url'],
			item['type'],
			item['episodes'],
			item['start_date'],
			item['end_date'],
			item['score']
		)
		# insert data into table
		c.execute('''INSERT OR REPLACE INTO anime(id, rank, title, image, type, episodes, start_date, end_date, score)
						VALUES(?,?,?,?,?,?,?,?,?)''', values)
	# 1 second pause to avoid API overload
	time.sleep(5)

# commit changes and exit
conn.commit()
conn.close()
print("database updated")
