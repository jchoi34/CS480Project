'''
def GA():
    for node in graph:
        if node.neighbors < 2:
            remove(node, graph)
    graphs.add(graph)
    while not graphs[i].isEmpty():
        maxVertex = test_node # this node has neighbor_count == 5
        for node in graphs[i]:
            if degree(node) > degree(maxVertex):
                manVertex = node
        F = F.add(maxVertex)
        V = V.remove(maxVertex)
        i += 1
        for node in graphs[i]:
            if node.neighbors < 2:
                remove(node, graph)
'''


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = None

    def __str__(self):
        return self.name


def weigh(A, B):
    return 1


def degree(vertex):
    return len(vertex.neighbors)


# prints the graph
def show_all(graph):
    for node in graph:
        for neighbor in node.neighbors:
            print(neighbor)

def m_print(obj):
    if type(obj) is Node:
        foo = str(obj) + ":"
        for neighbor in obj.neighbors:
            foo = foo + " " + str(neighbor.name)
        print(foo)
    if type(obj) is list:   # when obj is graph
        for node in obj:
            m_print(node)


# removes node from graph with deg < degree
def remove(graph, degree):
    copy = []
    for node in graph:
        length = len(node.neighbors)
        if length >= degree:
            node_copy = Node(node.name)
            for neighbor in node.neighbors:
                length_b = len(neighbor.neighbors)
                if length_b >= degree:
                    node_copy.neighbors.append(neighbor)
            copy.append(node_copy)
    return copy


if __name__ == "__main__":
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    a.neighbors = [b, c, e]
    b.neighbors = [a, e, f]
    c.neighbors = [a, e, f]
    d.neighbors = [f]
    e.neighbors = [a, b, c, f]
    f.neighbors = [b, c, d, e]

    graph = [a, b, c, d, e, f]
    m_print(remove(graph, 3))
