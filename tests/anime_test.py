from anime import Anime
from tree import AnimeNode
from jikan import Jikan

jikan = Jikan()
data = jikan.anime(19815)
data2 = jikan.anime(37450)
anime = Anime(data)
anime2 = Anime(data2)

node = AnimeNode(anime)
