A = ["A","B", "C", "E"];
B = ["B","A", "E", "F"];
C = ["C","A", "E", "F"];
D = ["D","F"];
E = ["E","A","B", "C", "F"];
F = ["F","B", "C", "D", "E"];
graph = [A,B,C,D,E,F];
cutset = [];

def remove(v,g):
    g.remove(v) #remove the node from graph
    for x in g:
        for i in x:
            if i == str(v[0]):  #remove any other isntances of the node
                x.remove(i) 

for x in graph:
    if len(x) < 3: #if degree is 1 or 0, remove from graph
        remove(x, graph)
while len(graph) != 0:
    maxDegree = 0 # init for max
    maxNode = graph[0] 
    for node in graph:
        if len(node) > maxDegree:
            maxDegree = len(node)
            maxNode = node
    cutset.append(maxNode)
    remove(maxNode,graph)
    for x in graph:
        if len(x) < 3: #if degree is 1 or 0, remove from graph
            remove(x, graph)
