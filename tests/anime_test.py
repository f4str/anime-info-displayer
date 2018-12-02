from api.anime.anime import Anime
from api.anime.tree import AnimeNode
from api.jikan.jikan import Jikan

jikan = Jikan()
data = jikan.anime(19815)
data2 = jikan.anime(37450)
anime = Anime(data)
anime2 = Anime(data2)

node = AnimeNode(anime)
