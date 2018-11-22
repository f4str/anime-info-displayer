import requests
from api.constants import *
from api.exceptions import ParameterError, ResponseError

session = requests.Session()


class Jikan:
	"""
	Class used to make API requests to the Jikan server and return json
	"""
	
	def __init__(self):
		"""
		Constructor for API caller
		"""
		self.anime_endpoint = BASE_URL + ENDPOINTS['anime']
		self.manga_endpoint = BASE_URL + ENDPOINTS['manga']
		self.person_endpoint = BASE_URL + ENDPOINTS['person']
		self.character_endpoint = BASE_URL + ENDPOINTS['character']
		self.search_endpoint = BASE_URL + ENDPOINTS['search']
		self.season_endpoint = BASE_URL + ENDPOINTS['season']
		self.archive_endpoint = BASE_URL + ENDPOINTS['archive']
		self.schedule_endpoint = BASE_URL + ENDPOINTS['schedule']
		self.top_endpoint = BASE_URL + ENDPOINTS['top']
		self.genre_endpoint = BASE_URL + ENDPOINTS['genre']
	
	def anime(self, anime_id, request=""):
		"""
		Gets anime specified by id
		:param anime_id: int
		:param request: string (optional)
		:return: json
		"""
		# check if valid anime id
		if anime_id < 1:
			raise ParameterError("Invalid Anime ID")
		# check if valid anime request
		if request.lower() not in ANIME_REQUEST:
			raise ParameterError("Invalid Anime Request")
		
		url = self.anime_endpoint.format(anime_id=anime_id, request=request)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def manga(self, manga_id, request=""):
		"""
		Gets manga specified by id
		:param manga_id: int
		:param request: string (optional)
		:return: json
		"""
		# check if valid manga id
		if manga_id < 1:
			raise ParameterError("Invalid Manga ID")
		# check if valid manga request
		if request.lower() not in ANIME_REQUEST:
			raise ParameterError("Invalid Manga Request")
		
		url = self.manga_endpoint.format(anime_id=manga_id, request=request)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def person(self, person_id):
		"""
		Gets person specified by id
		:param person_id: int
		:return: json
		"""
		# check if valid person id
		if person_id < 1:
			raise ParameterError("Invalid Person ID")
		
		url = self.person_endpoint.format(person_id=person_id)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def character(self, character_id):
		"""
		Gets character specified by id
		:param character_id:
		:return: json
		"""
		# check if valid person id
		if character_id < 1:
			raise ParameterError("Invalid Person ID")
		
		url = self.character_endpoint.format(character_id=character_id)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def top(self, category, page=1, subtype=""):
		"""
		Gets top anime/manga/person/character
		:param category: string
		:param page: int (optional)
		:param subtype: string
		:return: json
		"""
		# check if valid category
		if category.lower() not in CATEGORY:
			raise ParameterError("Invalid Category")
		# check if page is a valid number
		if page < 1:
			raise ParameterError("Invalid Page Number")
		# check if valid subtype
		if subtype.lower() not in SUBTYPE:
			raise ParameterError("Invalid Subtype")
		
		url = self.top_endpoint.format(category=category, page=page, subtype=subtype)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def genre(self, genre_type, genre, page=1):
		"""
		Gets top anime/manga based on specified genre id
		:param genre_type: "anime" or "manga"
		:param genre: int or string
		:param page: int
		:return: json
		"""
		# check if valid genre type
		if genre_type.lower() not in ("anime", "manga"):
			raise ParameterError("Invalid Genre Category")
		# check if valid page number
		if page < 1:
			raise ParameterError("Invalid Page Number")
		
		if isinstance(genre, int):
			# genre by id
			if genre < 1 or genre > 41:
				raise ParameterError("Invalid Genre ID")
			genre_id = genre
		else:
			# genre by name
			if genre not in GENRE:
				raise ParameterError("Invalid Genre")
			genre_id = GENRE[genre]
		
		url = self.genre_endpoint.format(genre_type=genre_type, genre_id=genre_id, page=page)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def season(self, year, season):
		"""
		Gets seasonal anime based on year and season
		:param year: int
		:param season: string
		:return: json
		"""
		# check if valid season
		if season not in SEASON:
			raise ParameterError("Invalid Season")
		
		url = self.season_endpoint.format(year=year, season=season)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def archive(self):
		"""
		Gets archive for years and seasons
		:return: json
		"""
		response = session.get(self.archive_endpoint)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def schedule(self, day=""):
		"""
		Gets schedule for current airing anime
		:param day: string
		:return: json
		"""
		# check if valid day
		if day not in DAY:
			raise ParameterError("Invalid Day")
		
		url = self.season_endpoint.format(day=day)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	def search(self, category, name):
		"""
		Gets matching results based on name
		:param category: string
		:param name: string
		:return: json
		"""
		# check if valid category
		if category not in CATEGORY:
			raise ParameterError("Invalid Category")
		
		url = self.search_endpoint.format(category=category, name=name)
		response = session.get(url)
		
		# check if valid response
		Jikan.check_response(response)
		
		return response.json()
	
	@classmethod
	def check_response(cls, response):
		"""
		Checks if any error message from json response
		:param response: json
		:return: void
		"""
		code = response.status_code
		if code in ERROR_RESPONSES:
			raise ResponseError(str(code) + ERROR_RESPONSES[code])
