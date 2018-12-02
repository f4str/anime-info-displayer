class AnimeNode:
	"""
	Node object for anime tree
	"""
	
	def __init__(self, anime):
		"""
		Constructor for node object requires anime object
		:param anime: Anime
		"""
		self.anime = anime
		self.parent = None
		self.children = []
	
	def add_child(self, anime):
		"""
		Adds child anime to node
		:param anime: Anime
		:return: AnimeNode
		"""
		if self.anime == anime:
			return None
		node = AnimeNode(anime)
		if node in self.children:
			return None
		self.children.append(node)
		node.parent = self
		return node
	
	def remove_child(self, anime):
		"""
		Removes child anime from node
		:param anime: AnimeNode
		:return: AnimeNode
		"""
		return self.children.remove(anime)
	
	def add_parent(self, anime):
		"""
		Adds parent anime to node
		:param anime: Anime
		:return: AnimeNode
		"""
		if self.anime == anime:
			return None
		node = AnimeNode(anime)
		self.parent = node
		node.children.append(self)
		return node
	
	def __eq__(self, other):
		return self.anime == other.anime
	
	def __ne__(self, other):
		return self.anime != other.anime
	
	def __hash__(self):
		return hash(self.anime)


class AnimeTree:
	"""
	Anime finder tree object
	"""
	
	def __init__(self, anime):
		"""
		Constructor for Anime Tree requires root node
		:param anime: Anime
		"""
		self.root = AnimeNode(anime)
		self.size = 0
		
	def add_child(self, child, parent):
		"""
		Adds anime node to specified parent node
		:param child: Anime
		:param parent: AnimeNode
		:return: AnimeNode
		"""
		node = parent.add_child(child)
		if node is not None:
			self.size += 1
		return node
	
	def add_parent(self, parent, child):
		"""
		Adds anime node to specified child node as parent and adjusts root
		:param parent: Anime
		:param child: AnimeNode
		:return: AnimeNode
		"""
		node = child.add_parent(parent)
		if node is not None:
			self.size += 1
		if child == self.root:
			self.root = self.root.parent
		return node
	
	def remove_child(self, child, parent):
		"""
		Removes anime node from specified parent node
		:param child: AnimeNode
		:param parent: AnimeNode
		:return: AnimeNode
		"""
		node = parent.remove_child(child)
		if node is not None:
			self.size -= 1
		return node
