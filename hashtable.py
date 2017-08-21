"""
Chaing Hash Table implementation using linked lists. 
Based on Professor Ernest Davis's notes on Hash Tables.
"""

class MyNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

	def __str__(self):
		if self.next != None:
			return "Node[" + self.key + " : " + str(self.value) + "] -> " + str(self.next)
		else:
			return "Node[" + self.key + " : " + str(self.value) + "]"
		# return "Node[" + self.key + " : " + str(self.value) + "] -> " + str(self.next)

class MyHashTable:
	def __init__(self, size=17):
		self.table = [None] * size
		
	def myHash(self, s):
		assert type(s) == str
		mult = 37
		remainder = len(self.table) % mult
		if remainder == 0 or remainder == 1 or remainder == len(self.table)-1:
			mult = 43
		sum_ = 0
		for i in xrange(len(s)):
			sum_ = (mult * sum_ + ord(s[i])) % len(self.table)
		return sum_

	def findNode(self, key, index):
		N = self.table[index]
		while N != None and N.key != key:
			N = N.next
		return N

	def insert(self, key, value):
		index = self.myHash(key)
		# print index
		if self.findNode(key, index) == None:
			newNode = MyNode(key, value)
			newNode.next = self.table[index]
			self.table[index] = newNode

	def retrieve(self, key):
		index = self.myHash(key)
		N = self.findNode(key, index)
		if N == None:
			return None
		else:
			return N.value

	def exists(self, key):
		if self.retrieve(key) == None:
			return False
		else:
			return True

	def __str__(self):
		return str([str(item) for item in self.table])

def announce(hash_table, key):
	print "Hashed " + str(hash_table.retrieve(key)) + " under " + key + " at index " + str(hash_table.myHash(key))

def run():
	hash_table = MyHashTable(7)
	hash_table.insert("Elon", "Musk")
	announce(hash_table, "Elon")
	hash_table.insert("Howard", "Hughes")
	announce(hash_table, "Howard")
	hash_table.insert("Walt", "Disney")
	announce(hash_table, "Walt")
	hash_table.insert("John", "Rockefeller")
	announce(hash_table, "John")
	hash_table.insert("Andrew", "Carnegie")
	announce(hash_table, "Andrew")
	hash_table.insert("Steve", "Jobs")
	announce(hash_table, "Steve")
	hash_table.insert("Bill", "Gates")
	announce(hash_table, "Gates")
	print hash_table.exists('Bill')
	# print hash_table.retrieve("Howard")
	print hash_table
	# n = MyNode('Elon', 'Musk')
	# n.next = MyNode('Larry', 'Page')
	# print n

run()