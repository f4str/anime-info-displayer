from collections import deque
from api.anime.tree import AnimeTree
from api.anime.anime import Anime
from api.anime.constants import *
from api.jikan.jikan import Jikan


def make_tree(anime):
	"""
	Creates anime tree
	:param anime: Anime
	:return: AnimeTree
	"""
	tree = AnimeTree(anime)
	queue = deque()
	root = tree.root
	queue.appendleft(root)
	visited = {root}
	
	while len(queue) > 0:
		current = queue.pop()
		related = current.anime.related
		for dependency in related:
			if dependency in CHILDREN:
				for item in related[dependency]:
					child = Anime(jikan.anime(item['mal_id']))
					node = current.add_child(child)
					visited.add(child)
					queue.appendleft(node)
	
	return tree


jikan = Jikan()
data = jikan.anime(27899)
anime1 = Anime(data)

tree1 = make_tree(anime1)
