# Node data structure to represent territory on the map
class Node:
        def __init__(self, name):
                self.name = name
                self.neighbors = []
                self.domain = ["Red", "Blue", "Green", "Yellow"]
		self.degree = 0

	def __str__(self):
		return self.name

	def get_domain(self):
		string = ""
		for i in self.domain:
			string += i + " "
		return self.name + " " + string

        def update_neighbors(self, assignment):
                for i in self.neighbors:
			if(not i.domain):
				return False
                        if(assignment in i.domain):
                                i.domain.remove(assignment)

	def reset_domain(self):
		self.domain = ["Red", "Blue", "Green", "Yellow"]

	def degrees(self):
		return len(self.neighbors)

	def is_empty(self):
		return not self.domain
