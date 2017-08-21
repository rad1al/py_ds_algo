from pprint import pformat
# pprint(g.graph)

class Graph:
	"""Graph implementation with dicts and sets."""
	def __init__(self, connections, directed=False):
		self.graph = dict()
		self.directed = directed
		self.add_connections(connections)

	def add_connections(self, connections):
		for node1, node2 in connections:
			self.add(node1, node2)

	def add(self, node1, node2):
		if node1 not in self.graph:
			self.graph[node1] = set()
			self.graph[node1].add(node2)
		else:
			self.graph[node1].add(node2)
		if self.directed == False:
			if node2 not in self.graph:
				self.graph[node2] = set()
				self.graph[node2].add(node1)
			else:
				self.graph[node2].add(node1)
	def remove(self, node):
		for k in self.graph:
			try:
				self.graph[k].remove(node)
			except KeyError:
				pass
		try:
			del self.graph[node]
		except KeyError:
			pass

	def find_path(self, node1, node2, path=[]):
		path = path + [node1]
		if node1 == node2:
			return path
		if node1 not in self.graph:
			return None
		for node in self.graph[node1]:
			if node not in path:
				new_path = self.find_path(node, node2, path)
				if new_path:
					return new_path
		return None

	def is_connected(self, node1, node2):
		"""Is node1 directly connected to node2?"""
		if node1 in self.graph:
			if node2 in self.graph[node1]:
				return True
		return False

	def __str__(self):
		# return ''.join(['Graph:\n'] + ["{0} : {{{1}}}\n".format(k,','.join(self.graph[k])) for k in self.graph])
		return "{0}\n{1}".format(self.__class__.__name__, pformat(self.graph, width=60))

connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
                   ('C', 'D'), ('E', 'F'), ('F', 'C')]

g = Graph(connections, directed=True)
print g
g.remove('C')
print g

g = Graph(connections)
# print g
g.add('E', 'D')
# print g
g.remove('A')
g.add('G', 'B')
print g
print g.find_path('G', 'E')









