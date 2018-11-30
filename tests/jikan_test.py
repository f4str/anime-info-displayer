from jikan import Jikan

jikan = Jikan()
# response = jikan.anime(19815)
# response2 = jikan.genre("anime", 2)
# response3 = jikan.genre("manga", "slice of life")
# response4 = jikan.archive()
# response5 = jikan.search("anime", "Sword Art Online")
#
# print(json.dumps(response, indent=4))

ids = [19815, 37430, 11757, 5114, 1535, 1575, 9253, 28851, 1]

for i in ids:
	response = jikan.anime(i)
	print(response['title'])
