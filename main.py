import sys
import os


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

    def __str__(self):
        return self.name


def weigh(A, B):
    return 1


def degree(vertex):
    return len(vertex.neighbors)


def remove(graph, degree):
    for node in graph:
        if len(node.neighbors) < degree:
            graph.remove(node)
    return graph


def show_all(graph):
    for node in graph:
        for neighbor in node.neighbors:
            print(neighbor)


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

    show_all(remove(graph, 5))  # should print none, but prints..... wtf?
