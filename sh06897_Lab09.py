import numpy as np

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    
    return G
#print(addNodes({},['BOS', 'ORD', 'JFK', 'DFW', 'MIA', 'SFO', 'LAX']))


def addEdges(G, edges, directed):
    for i in edges:
        if directed:
            G[i[0]].append((i[1],i[2]))
        else:
            G[i[0]].append((i[1],i[2]))
            G[i[1]].append((i[0],i[2]))
    return G
#print(addEdges(G, edges, True)) 

def listOfNodes(G):
    print([*G])
#listOfNodes(G)

def listOfEdges(G,directed):
    lst =[]
    sets = []
    for i in G.keys():
        edges = G.get(i)
        for E in edges:
            if directed:
                sets.append((i,E[0],E[1]))
            else:
                if (E[0],i,E[1]) not in sets:
                    sets.append((i,E[0],E[1]))
    lst += sets
    sets = []
    print(lst)
#listOfEdges(G,True)

def printIn_OutDegree(G):
    for key, value in G.items():
        Incount = Outcount = 0 
        Outcount = len(value)
        for i in G.values():
            for j in i:
                if key == j[0]:
                    Incount += 1
        print(f"{key} => In-Degree: {Incount}, Out-Degree: {Outcount}")
#printIn_OutDegree(G)

def printDegree(G):
    for key, value in G.items():
        print(f"{key} => {len(value)}")
        pass
#printDegree(G)

def getNeighbors(G, node):
    lst = []
    for j in G.get(node):
        lst.append(j[0])
    print(lst)
#getNeighbors(G, 'BOS')            

def getInNeighbors(G, node):
    lst = []
    for key, value in G.items():
        for i in value:
            if i[0] == node:
                lst.append(key)
    print(lst)
#getInNeighbors(G, 'BOS')

def getOutNeighbors(G, node):
    lst = []
    for i in G.get(node):
        lst.append(i[0])
    print(lst)
#getOutNeighbors(G, 'BOS')

def getNearestNeighbor(G, node):
    min = G.get(node)[0][1]
    for i in G.get(node):
        if i[1] <= min:
            min = i[1]
            ans = i[0]
    print(ans)
#getNearestNeighbor(G, 'BOS')

def isNeighbor(G, Node1, Node2):
    lst = [i[0] for i in G.get(Node1)]
    return(Node2 in lst)         
#print(isNeighbor(G, 'DFW', 'MIA'))

def removeNode(G, node):
    del G[node]
    for i in G.values():
        for j in i:
            if j[0] == node:
                i.pop(i.index(j))
    print(G)
#removeNode(G, 2)

def removeNodes(G, nodes):
    for select in nodes:
        del G[select]
        for i in G.values():
            for j in i:
                if j[0] == select:
                    i.pop(i.index(j))
    print(G)
#removeNodes(G, [1, 2])

def displayGraph(G):
    print(G)
#displayGraph(G)


def display_adj_matrix(G):
    matrix = [ [ 0 for i in range(len(G.keys())) ] for j in range(len(G.keys())) ]
    keys = [*G]
    for x in G.keys():
        for y in G.get(x):
            matrix[keys.index(x)][keys.index(y[0])] = y[1]
    print(np.array(matrix))
#display_adj_matrix(G)

