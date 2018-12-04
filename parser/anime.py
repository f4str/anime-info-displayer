class Anime:
	"""
	Anime object containing information about the anime
	"""
	
	def __init__(self, data):
		"""
		Constructor for anime object requires json object
		:param data: json
		"""
		self.mal_id = data['mal_id']
		self.title = data['title']
		self.title_english = data['title_english']
		self.image = data['image_url']
		self.type = data['type']
		self.source = data['source']
		self.airing = data['airing']
		self.rating = data['rating']
		self.duration = data['duration']
		self.score = data['score']
		self.episodes = data['episodes']
		self.rank = data['rank']
		self.popularity = data['popularity']
		self.synopsis = data['synopsis']
		self.premiered = data['premiered']
		self.broadcast = data['broadcast']
		self.startdate = data['aired']['prop']['from']
		self.enddate = data['aired']['prop']['to']
		self.studio = data['studios'][0]['name']
		self.genres = Anime.get_genres(data['genres'])
		self.openings = Anime.get_songs(data['opening_themes'])
		self.endings = Anime.get_songs(data['ending_themes'])
		self.related = data['related']
	
	def __eq__(self, other):
		return self.mal_id == other.mal_id
	
	def __ne__(self, other):
		return self.mal_id != other.mal_id
	
	def __hash__(self):
		return hash(self.mal_id)
	
	def __str__(self):
		return str(self.__dict__)
	
	def __repr__(self):
		return str(self.__dict__)
	
	@classmethod
	def get_genres(cls, data):
		"""
		Get list of anime genres
		:param data: json
		:return: dict
		"""
		genres = {}
		for genre in data:
			genres[genre['name']] = genre['mal_id']
		return sorted(genres)
	
	@classmethod
	def get_songs(cls, data):
		"""
		Get opening/ending songs from json
		:param data: json
		:return: list
		"""
		songs = []
		for song in data:
			split = song.split('"')
			if len(split) > 1:
				songs.append(split[1])
		return songs
