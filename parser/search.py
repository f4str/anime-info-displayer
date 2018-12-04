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
	# queue for BFS
	queue = deque()
	root = tree.root
	queue.appendleft(root)
	# set for keeping track of visited anime
	visited = {anime}
	
	# BFS downwards
	while len(queue) > 0:
		current = queue.pop()
		related = current.anime.related
		for relation in related:
			if relation.lower() in CHILDREN:
				for item in related[relation]:
					child = Anime(jikan.anime(item['mal_id']))
					node = tree.add_child(child=child, parent=current)
					visited.add(node)
					queue.appendleft(child)
	
	parent_id = 0
	# Search for parent upwards
	while parent_id is not None:
		related = root.anime.related
		parent_id = None
	
		for i in PARENT:
			if i in related:
				parent_id = related[i][0]['mal_id']
				break
		
		if parent_id is None:
			break
			
		parent = Anime(jikan.anime(parent_id))
		node = tree.add_parent(parent=parent, child=root)
		root = node
		visited.add(root)
		queue.appendleft(parent)
		
		# BFS new root
		while len(queue) > 0:
			current = queue.pop()
			if current is None:
				continue
			related = current.anime.related
			for relation in related:
				if relation.lower() in CHILDREN:
					for item in related[relation]:
						child = Anime(jikan.anime(item['mal_id']))
						node = tree.add_child(child=child, parent=current)
						if node in visited:
							continue
						visited.add(node)
						queue.appendleft(child)
						
	return tree
	

if len(sys.argv) > 1:
	id = int(sys.argv[1])
else:
	id = 33486

jikan = Jikan()
data = jikan.anime(id)
anime = Anime(data)

print(json.dumps(anime.__dict__))

#tree = make_tree(anime)

sys.stdout.flush()
