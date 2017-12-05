from node import *
from tree_CSP_Solver import *

C = Node("C")
B = Node("B")
D = Node("D")

tree = [C,B,D]

assignment = tree_solver(tree)
if(assignment != False):
	for i in range(0, len(tree)):
		print tree[i].name + " color: " + assignment[i]
