

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = None

    def __str__(self):
        return self.name


def weigh(A, B):
    return 1


def degree(node):
    return len(node.neighbors)


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
def remove_less_than(graph, degree):
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

def remove(graph, node_a):
    copy = []
    for node_b in graph:
        if node_b.name != node_a.name:
            node_copy = Node(node_b.name)
            for neighbor in node_b.neighbors:
                if neighbor.name != node_a.name:
                    node_copy.neighbors.append(neighbor)
            copy.append(node_copy)
    return copy


def find_maxVertex(graph):
    maxVertex = Node('TEST')
    for node in graph:
        if degree(node) > degree(maxVertex):
            maxVertex = node
    return maxVertex



def GA(graph):
    graphs = []
    i = 0
    F = []

    graph = remove_less_than(graph, 2)

    while True:
        v = find_maxVertex(graph)
        F.append(v)
        graph = remove(graph, v)
        graph = remove_less_than(graph, 2)
        length = len(graph)
        if length == 0:
            break
    print("F")
    m_print(F)
    return F


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
    GA(graph)
