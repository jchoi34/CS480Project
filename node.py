class Node:
        def __init__(self, name):
                self.name = name
                self.neighbors = []
                self.domain = ["Red", "Blue", "Green", "Yellow"]
		self.degree = 0

	def __str__(self):
		return self.name

        def update_neighbors(self, assignment):
                for i in range (0, self.degrees()):
			if(not self.neighbors[i].domain):
				return False
                        if(assignment in self.neighbors[i].domain):
                                self.neighbors[i].domain.remove(assignment)

	def degrees(self):
		return len(self.neighbors)

	def is_empty(self):
		return not self.domain
