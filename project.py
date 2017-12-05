A = ["A","B", "C", "E"];
B = ["B","A", "E", "F"];
C = ["C","A", "E", "F"];
D = ["D","F"];
E = ["E","A","B", "C", "F"];
F = ["F","B", "C", "D", "E"];
graph = [A,B,C,D,E,F];
cutset = [];

def remove(v,g):
    g.remove(v)
    print(str(v[0]));
    for x in g:
        for i in x:
            if i == str(v[0]):
                x.remove(i) 

for x in graph:
    if len(x) < 3:
        remove(x, graph)  
