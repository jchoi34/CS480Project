class Node:
        def __init__(self, name):
                self.name = name
                self.neighbors = []
                self.domain = ["Red", "Blue", "Green", "Yellow"]

        def update_neighbors(self, assignment):
                for i in self.neighbors:
                        if(self.neighbors[i].domain.contains(assignment)):
                                self.neighbors[i].domain.remove(assignment)

