import os
os.chdir(os.path.join(os.path.abspath(os.path.curdir), 'src/jikan'))
import sys
import json
from jikan import Jikan


jikan = Jikan()

if len(sys.argv) > 1:
	title = sys.argv[1]
	response = jikan.search('anime', title)
	results = response['results']
else:
	response = jikan.top('anime', 'bypopularity')
	results = response['top']

for entry in results:
	print(json.dumps(entry))

sys.stdout.flush()
