BASE_URL = "http://api.jikan.moe/v3"

ENDPOINTS = {
	"anime": "/anime/{anime_id}/{request}",
	"manga": "/manga/{manga_id}/{request}",
	"person": "/person/{person_id}",
	"character": "/character/{character_id}",
	"search": "/search/{category}?q={name}",
	"season": "/season/{year}/{season}",
	"archive": "/season/archive",
	"schedule": "/schedule/{day}",
	"top": "/top/{category}/{page}/{subtype}",
	"genre": "/genre/{genre_type}/{genre_id}/{page}"
}

ERROR_RESPONSES = {
	400: "Bad Request",
	404: "Not Found",
	405: "Method Not Allowed",
	429: "Too Many Requests"
}

SEASON = {"winter", "spring", "fall", "summer"}
CATEGORY = {"anime", "manga", "person", "characters"}
SUBTYPE = {"", "airing", "upcoming", "tv", "movie", "ova", "special", "bypopularity", "favorite"}
ANIME_REQUEST = {"", "characters_staff", "episodes", "news", "pictures", "videos", "stats", "forum", "moreinfo"}
MANGA_REQUEST = {"", "characters", "news", "pictures", "stats", "forum", "moreinfo"}
DAY = {"", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "other", "unknown"}

GENRE = {
	"action": 1,
	"adventure": 2,
	"cars": 3,
	"comedy": 4,
	"dementia": 5,
	"demons": 6,
	"mystery": 7,
	"drama": 8,
	"ecchi": 9,
	"fantasy": 10,
	"game": 11,
	"hentai": 12,
	"historical": 13,
	"horror": 14,
	"kids": 15,
	"magic": 16,
	"martial_arts": 17,
	"mecha": 18,
	"music": 19,
	"parody": 20,
	"samurai": 21,
	"romance": 22,
	"school": 23,
	"sci fi": 24,
	"shoujo": 25,
	"shoujo ai": 26,
	"shounen": 27,
	"shounen ai": 28,
	"space": 29,
	"sports": 30,
	"super power": 31,
	"vampire": 32,
	"yaoi": 33,
	"yuri": 34,
	"harem": 35,
	"slice of life": 36,
	"supernatural": 37,
	"military": 38,
	"police": 39,
	"psychological": 40,
	"thriller": 41
}
