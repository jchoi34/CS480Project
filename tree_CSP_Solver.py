from node import *

# tree = entire set of nodes in graph with the cutset removed
def tree_solver(tree):
	assignment = [0] * len(tree)
	for node in tree:
		if(not make_arc_consistent(node)):
			return False
	i = 0
	for node in tree:
		if(not node.domain):
			return False
		if(not node.neighbors):
			assignment[i] = node.domain[0]
		else:
			assignment[i] = node.domain[0]
			node.update_neighbors(assignment[i])
		i += 1
	return assignment

def make_arc_consistent(node):
	if(not node.neighbors):
		return True
	if(len(node.neighbors) > 1): # only update domains from children to parent
		return True		# to avoid redundant updating
	if(len(node.domain) == 1):
		if(node.domain[0] in node.neighbors[0].domain):
			node.neighbors[0].domain.remove(node.domain[0])
	elif(len(node.neighbors[0].domain) == 1):
		if(node.neighbors[0].domain[0] in node.domain):
			node.domain.remove(node.neighbors[0].domain[0])
	if(not node.neighbors[0].domain or not node.domain):
		return False

	return True

