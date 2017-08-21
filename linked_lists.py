class OrderedList:
	"""
	Singly linked list with header.
	"""
	def __init__(self, v=None, n=None):
		self.value = v
		self.next = n

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next

	def search_before(self, v):
		"""
		If v is in the list, return the previous node. Otherwise, find the node with 
		the greatest value less than v and return it.
		"""
		n = self
		while True:
			if n.next == None:
				return n
			if n.next.value >= v:
				# print n.value
				return n
			n = n.next

	def exists(self, v):
		n = self.search_before(v)
		return n.next != None and n.next.value == v

	def add(self, v):
		"""Adds v to the ordered list if it is not already there."""
		n = self.search_before(v)
		if n.next == None or n.next.value != v:
			new_node = OrderedList()
			new_node.value = v
			new_node.next = n.next
			# new_node = OrderedList(v, n.next)
			n.next = new_node

	def remove(self, v):
		n = self.search_before(v)
		if n.next != None and n.next.value == v:
			n.next = n.next.next

	def size(self):
		total = 0
		a = self.next
		while a != None:
			total += 1
			a = a.next
		return total

	def rsize(self):
		if self.next == None:
			return 0
		else:
			return self.next.rsize() + 1


	def __str__(self):
		a = self.next
		s = "[ "
		while a != None:
			s = s + str(a.value) + " "
			a = a.next
		return s + "]"

def run_ordered_list():
	print "Demonstration of OrderedList class:"
	lst = OrderedList()
	lst.add(20)
	lst.add(10)
	lst.add(30)
	print lst
	lst.add(5)
	lst.add(50)
	lst.add(25)
	lst.add(100)
	print lst
	lst.remove(50)
	lst.remove(22)
	print lst
	print "Does 20 exist in the list?:", lst.exists(20)
	print "Size of list (by iteration):", lst.size()
	print "Size of list (by recursion):", lst.rsize()

# run_ordered_list()

###############################################################################

class ArrayStack:
	"""Stack implemented with a fixed size array"""
	def __init__(self):
		self.stack = [None] * 100
		self.num_elements = 0

	def empty_stack(self):
		return self.num_elements == 0

	def top(self):
		return self.stack[self.num_elements - 1]

	def push(self, v):
		self.stack[self.num_elements] = v
		self.num_elements += 1

	def pop(self):
		self.num_elements -= 1
		return self.stack[self.num_elements]

def run_arraystack():
	arraystack = ArrayStack()
	arraystack.push(2)
	arraystack.push(3)
	arraystack.push(5)
	# print arraystack.stack
	print arraystack.top()
	print arraystack.pop()
	print arraystack.pop()
	arraystack.push(15)
	arraystack.push(22)
	# print arraystack.stack
	print arraystack.top()

###############################################################################

class FQNode:
	def __init__(self):
		self.value = None
		self.next = None


class FIFOQueue:
	def __init__(self):
		self.header = FQNode()
		self.last = self.header

	def empty(self):
		return self.header.next == None

	def add(self, v):
		n = FQNode()
		n.value = v
		self.last.next = n
		self.last = n

	def pop(self):
		v = self.header.next.value
		if self.header.next == None:
			self.last = self.header
		self.header.next = self.header.next.next
		return v

	def __str__(self):
		s = "[ <- "
		n = self.header.next
		while n != None:
			s = s + str(n.value) + " "
			n = n.next
		return s + "<- ]"

	def size(self):
		total = 0
		n = self.header.next
		while n != None:
			total += 1
			n = n.next
		return total

def run_fifo_queue():
	fq = FIFOQueue()
	fq.add(4)
	fq.add(14)
	fq.add(23)
	print fq.pop()
	fq.add(28)
	fq.add(34)
	print fq.pop()
	print fq
	print "Size:", fq.size()

# run_fifo_queue()

###############################################################################

class CircularArray:
	def __init__(self):
		pass # To be implemented later.

###############################################################################

class DLLNode:
	def __init__(self):
		self.value = None
		self.next = None
		self.previous = None

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next

	def get_previous(self):
		return self.previous

	def set_value(self, v):
		self.value = v
		return v
	
	def set_next(self, node):
		self.next = node
		return node

	def set_previous(self, node):
		self.previous = node
		return node

class DLList:
	def __init__(self):
		self.first = None
		self.last = None

	def is_empty(self):
		return self.first == None

	def get_first(self):
		return self.first

	def get_last(self):
		return self.last

	def set_first(self, node):
		self.first = node

	def set_last(self, node):
		self.last = node
	
	def add_first(self, v):
		n = DLLNode()
		n.set_value(v)
		if self.is_empty():
			self.last = n
		else:
			n.set_next(self.first)
			self.first.set_previous(n)
		self.first = n

	def add_last(self, v):
		n = DLLNode()
		n.set_value(v)
		if self.is_empty():
			self.first = n
		else:
			n.set_previous(self.last)
			self.last.set_next(n)
		self.last = n

	def get_item(self, index):
		w = self.first
		i = 0
		while i < index:
			w = w.get_next()
			i += 1
		return w

	def get_value(self, index):
		return self.get_item(index).get_value()

	def add_after(self, a, v):
		"""Add v after node a"""
		n = DLLNode()
		n.set_value(v)
		n.set_next(a.get_next())
		a.get_next().set_previous(n)
		n.set_previous(a)
		a.set_next(n)
		if a == self.last:
			self.last = n

	def add_before(self, a, v):
		n = DLLNode()
		n.set_value(v)
		n.set_previous(a.get_previous())
		a.get_previous().set_next(n)
		n.set_next(a)
		a.set_previous(n)
		if a == self.first:
			self.first = n

	def remove(self, node):
		# if node == None:
		# 	return None
		if self.first == node:
			self.first = node.get_next()
		else:
			node.get_previous().set_next(node.get_next())
		if self.last == node:
			self.last == node.get_previous()
		else:
			node.get_next().set_previous(node.get_previous())

	def __str__(self):
		if self.first == None:
			return "[]"
		n = self.first
		s = "[ "
		while n.get_next() != None:
			s = s + str(n.get_value()) + " "
			n = n.get_next()
		return s + str(n.get_value()) + "]"

	def find(self, v):
		n = self.first
		while n != self.last:
			if n.get_value() == v:
				return n
			else:
				n = n.get_next()
		if self.last.get_value() == v:
			return self.last
		else:
			return None

	def size(self):
		total = 0
		n = self.first
		while n != None:
			total += 1
			n = n.get_next()
		return total


def run_dll_list():
	print "Initializing doubly linked list:"
	dll = DLList()
	print dll
	print "Size:", dll.size()
	dll.add_first("Once")
	dll.add_last("Upon")
	dll.add_last("A")
	dll.add_last("Time")
	print dll
	print "Replacing value at index 0 with \"Twice\":"
	dll.get_item(0).set_value("Twice")
	print dll 
	dll.add_after(dll.get_item(0), "?")
	print dll
	dll.remove(dll.find("A"))
	print dll
	print "Size:", dll.size()
	dll.add_before(dll.find("Time"), "Some")
	print dll
	print dll.get_value(3)

run_dll_list()





























