from collections import deque
from tree import AnimeTree
from anime import Anime
from constants import *
from jikan import Jikan
import sys
import json


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


if len(sys.argv) > 1:
	id = int(sys.argv[1])
else:
	id = 31964

jikan = Jikan()
data = jikan.anime(id)
anime = Anime(data)

print(json.dumps(anime.__dict__))

sys.stdout.flush()
