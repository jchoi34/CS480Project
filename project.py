A = ["A","B", "C", "E"];
B = ["B","A", "E", "F"];
C = ["C","A", "E", "F"];
D = ["D","F"];
E = ["E","A","B", "C", "F"];
F = ["F","B", "C", "D", "E"];
graph = [A,B,C,D,E,F];
cutset = [];

def remove(v,g): #helper function that removes the node from main graph and other lists that contain it
    g.remove(v) #remove the node from graph
    print(str(v[0]));
    for x in g:
        for i in x:
            if i == str(v[0]):  #remove any other isntances of the node
                x.remove(i) 

for x in graph:
    if len(x) < 3: #if degree is 1 or 0, remove from graph
        remove(x, graph)
while len(graph) != 0: #while graph is not empty
    maxDegree = 0 # init for maxDegree value
    maxNode = graph[0] #init for maxNode refrence
    for node in graph: 
        if len(node) > maxDegree:  #find highest degree node and store it
            maxDegree = len(node)
            maxNode = node
    cutset.append(maxNode) #add this node to the cutset
    remove(maxNode,graph) #remove all refrences from original graph
    for x in graph:
        if len(x) < 3: #if degree is 1 or 0, remove from graph
            remove(x, graph)
