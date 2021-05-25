import numpy as np

# Exercise # 1 ---------------->

'''edges = [(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]
nodes = [1, 2, 3, 4, 5]

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    
    return G
G = addNodes({}, nodes)

def addEdges(G, edges, directed):
    for i in edges:
        if directed:
            G[i[0]].append((i[1],i[2]))
        else:
            G[i[0]].append((i[1],i[2]))
            G[i[1]].append((i[0],i[2]))
    return G
G = addEdges(G, edges, False)

def listOfNodes(G):
    print("Nodes =",[*G])

listOfNodes(G)

def listOfEdges(G, directed):
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
    print("Edges =",lst)
listOfEdges(G, False)


def display_adj_matrix(G):
    matrix = [ [ 0 for i in range(len(G.keys())) ] for j in range(len(G.keys())) ]
    keys = [*G]
    for x in G.keys():
        for y in G.get(x):
            matrix[keys.index(x)][keys.index(y[0])] = y[1]
    print(np.array(matrix))
display_adj_matrix(G)

def displayGraph(G):
    print(G)
displayGraph(G)

def getNeighbors(G, node):
    for i in node:
        lst = []
        for j in G.get(i):
            lst.append(j[0])
        print(f"{i}: neighbors => {lst}, Degree: {len(G.get(i))}")
getNeighbors(G, nodes) '''


# Exercise # 2 ----------------->

'''nodes = [1, 2, 3, 4]
edges = [(1, 2), (2, 4), (3, 1), (3, 2), (4, 3), (4, 4)]

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    
    return G
G = addNodes({}, nodes)

def addEdges(G, edges, directed):
    for i in edges:
        if directed:
            G[i[0]].append((i[1], 1))
        else:
            G[i[0]].append((i[1], 1))
            G[i[1]].append((i[0], 1))
    return G
G = addEdges(G, edges, True)

def displayGraph(G):
    print(G)
displayGraph(G)

def printIn_OutDegree(G):
    Out = In = 0
    for key, value in G.items():
        Incount = Outcount = 0 
        Outcount = len(value)
        Out += len(value)
        for i in G.values():
            for j in i:
                if key == j[0]:
                    Incount += 1
                    In += 1
        print(f"{key} => Out-Degree: {Outcount}, In-Degree: {Incount}")
    return In, Out
In, Out = printIn_OutDegree(G)



def getNeighbors(G, node):
    for i in node:
        lst = []
        for j in G.get(i):
            lst.append(j[0])
        print(f"{i} neighbors are {lst}")
getNeighbors(G, nodes) 

def sumCounter(In, Out, edges):
    return (In == Out and len(edges) == In)
print(sumCounter(In, Out, edges))''' 

# Exercise # 3 ------------->

nodes = ['Dallas', 'Austin', 'Washington', 'Denver', 'Atlanta', 'Chicago', 'Houston']
edges = [('Dallas', 'Austin', 200), ('Dallas', 'Denver', 780), ('Dallas', 'Chicago', 900), ('Austin', 'Dallas', 200), ('Austin', 'Houston', 160), ('Washington', 'Dallas', 1300), ('Washington', 'Atlanta', 600), ('Denver', 'Atlanta', 1400), ('Denver', 'Chicago', 1000), ('Atlanta', 'Washington', 600), ('Atlanta', 'Houston', 800), ('Chicago', 'Denver', 1000), ('Houston', 'Atlanta', 800)]

def addNodes(G, nodes):
    for i in nodes:
        G[i] = []
    
    return G
G = addNodes({}, nodes)


def addEdges(G, edges, directed):
    for i in edges:
        if directed:
            G[i[0]].append((i[1],i[2]))
        else:
            G[i[0]].append((i[1],i[2]))
            G[i[1]].append((i[0],i[2]))
    return G
G = addEdges(G, edges, True)


def displayGraph(G):
    print(G)
displayGraph(G)

def maxFlights(G):
    In_lst, Out_lst = [], []
    Finder = [*G]
    for key, value in G.items():
        Incount = 0 
        Out_lst.append(len(value))
        for i in G.values():
            for j in i:
                if key == j[0]:
                    Incount += 1
        In_lst.append(Incount)
    max_in , max_out = Finder[In_lst.index(max(In_lst))], Finder[Out_lst.index(max(Out_lst))]
    print("Maximum number of Outbound:",max_out)
    print("Maximum number of Inbound:",max_in)
maxFlights(G)

def oneWayAirports(G):
    output = []
    for node in [*G]:
        lst = [i[0] for i in G.get(node)]
        for j in lst:
            lstOfAir = [x[0] for x in G.get(j)]
            if not(node in lstOfAir):
                output.append((node,j))
    print(output)
oneWayAirports(G)

def nearestAirport(G):
    for node in [*G]:
        min = G.get(node)[0][1]
        for i in G.get(node):
            if i[1] <= min:
                min = i[1]
                ans = i[0]
        print(f"Nearest_Airport {node} will give: {ans}")
nearestAirport(G)

def allAirports(G, A):
    lst = []
    lst1 = []
    for key, value in G.items():
        for i in value:
            if i[0] == A:
                lst.append(key)
                for keys, value in G.items():
                    for j in value:
                        if j[0] in lst and keys != A:
                            lst1.append(keys)   
    print(lst+lst1)
allAirports(G, "Dallas")