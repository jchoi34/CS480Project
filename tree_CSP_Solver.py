def tree_solver(tree, domain, constraint):
	length = len(variables)
	root = tree[0] # can be any variable
	assignment = []
	#sorted_set = t_sort(tree)
	for i in range(length, 2, -1):
		if(not make_arc_consistent(tree[i].remainingDomain, tree[i].neighbors)):
			return False
	for i in range (0, length):
		if(not tree[i].remainingDomain):
			return False

		assignment = tree[i].remaningDomain[0]
		tree[i+1].update_neighbors(assignment)

	return assignment
		
def update_neighbors(self, assignment):
	for i in range(0, len(node.neighbors)):
		self.neighbors[i].remainingDomain.remove(assignment)
	

def make_arc_consistent(domain1, parent_nodes):
	if(not domain1 or not domain2):
		return False
	for i in range(0, len(domain1)):
		for j in range(0, len(domain2)):
			if (domain1[i] != domain2[j]):
				return True
	return False

def t_sort(tree):
	s = []

	
