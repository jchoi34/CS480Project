from node import *

# tree = entire set of nodes in graph with the cutset removed
def tree_solver(tree):
	assignment = [0] * len(tree)
	tree_copy = list(tree)
	for node in tree_copy:
		if(not make_arc_consistent(node)):
			return False
	i = 0
	for node in tree_copy:
		if(not node.domain):
			return False
		if(not node.neighbors):
			assignment[i] = node.domain[0]
		else:
			assignment[i] = node.domain[0]
			node.update_neighbors(assignment[i])
		i += 1
	return assignment

def make_arc_consistent(tree):
	if(not tree.neighbors):
		return True
	if(len(tree.neighbors) > 1): # only update domains from children to parent
		return True		# to avoid redundant updating
	if(len(tree.domain) == 1):
		if(tree.domain[0] in tree.neighbors[0].domain):
			tree.neighbors[0].remove(tree.domain[0])
	elif(len(tree.neighbors.domain) == 1):
		if(tree.neighbors[0].domain[0] in tree.domain):
			tree.domain.remove(tree.neighbors[0].domain[0])
	if(not tree.neighbors[0].domain or not tree.domain):
		return False

	return True

