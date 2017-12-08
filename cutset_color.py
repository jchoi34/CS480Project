from node import *
from random import randint

# function for coloring the cutset
# choose colors at random for the cutset nodes
# update its neighbors accordingly
# Output: False if a node/neighbor runs of of colors
# otherwise return coloring
def color_cutset(cutset):
	length = len(cutset)
	assignment = [0] * length

	i = 0
	for node in cutset:
		if(node.is_empty()):
			return False
		assignment[i] = node.domain[randint(0, len(node.domain)-1)]
		if(node.update_neighbors(assignment[i]) == False):
			return False
		i += 1

	return assignment


