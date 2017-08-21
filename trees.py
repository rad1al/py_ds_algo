class lstTree:
	"""
	Uses a Python list to store children. Has upward and downward pointers.
	"""
	def __init__(self, label):
		self.label = label
		self.parent = None
		self.children = list()
		self.num_of_children = 0

	def get_label(self):
		return self.label

	def get_parent(self):
		return self.parent

	def get_children(self):
		return self.children

	def get_num_of_children(self):
		return self.num_of_children

	def add_child(self, t):
		self.children.append(t)
		self.num_of_children += 1
		t.parent = self

	def display_preorder(self, indent):
		for i in xrange(indent):
			print " ",
		print str(self)
		# for j in xrange(self.num_of_children):
		# 	self.children[j].display_preorder(indent+3)
		for child in self.children:
			child.display_preorder(indent+3)

	def run_display_preorder(self):
		self.display_preorder(0)

	def display_postorder(self, indent):
		# for i in xrange(self.num_of_children):
		# 	self.children[i].display_postorder(indent+3)
		for child in self.children:
			child.display_preorder(indent+3)
		for j in xrange(indent):
			print " ",
		print str(self)

	def run_display_postorder(self):
		self.display_postorder(0)

	def __str__(self):
		return str(self.label)

def run_tree():
	animal_group = lstTree("Animal Group")
	mammal = lstTree("Mammal")
	carnivore = lstTree("Carnivore")
	rodent = lstTree("Rodent")
	primate = lstTree("Primate")
	squirrel = lstTree("Squirrel")
	rat = lstTree("Rat")
	cat = lstTree("Cat")
	dog = lstTree("Dog")
	skunk = lstTree("Skunk")
	gorilla = lstTree("Gorilla")
	human = lstTree("Human")
	animal_group.add_child(mammal)
	mammal.add_child(carnivore)
	mammal.add_child(rodent)
	mammal.add_child(primate)
	carnivore.add_child(cat)
	carnivore.add_child(dog)
	carnivore.add_child(skunk)
	rodent.add_child(rat)
	rodent.add_child(squirrel)
	primate.add_child(gorilla)
	primate.add_child(human)
	print "Preorder:"
	mammal.run_display_preorder()
	print "Postorder:"
	mammal.run_display_postorder()

run_tree()





