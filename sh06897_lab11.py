#Exercise # 1 ------------>
G={0:[1,2] , 1:[2,3], 2:[4] , 3:[4,5] , 4:[5] , 5:[]}
def depthFirstSearch(G, node):
    stack = [node]
    visited = []
    while len(stack) != 0:
        x = stack.pop()
        if x not in visited:
            visited.append(x)
            for j in G.get(x):
                stack.append(j)
    print(visited)

depthFirstSearch(G, 0)

#Exercise # 2 -------------->
G = {'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]} 
def check_cycles(G, lst):
    checker = []
    for j in range(len(lst)):
        for i in G.get(lst[j]):
            if j+1 < len(lst):
                if lst[j+1] == i[0]:
                    checker.append(1)
            else:
                if lst[0] == i[0]:
                    checker.append(1)
    return(len(checker) == len(lst))
#print(check_cycles(G, ['Austin','Houston','Atlanta','Washington','Dallas']))

#Exercise # 3 ------------>
G = {0:[1, 2], 1:[3, 4, 5], 2:[6], 3:[], 4:[], 5:[], 6:[7], 7:[]}
def breathFirstSearch(G, node):
    queue = [node]
    visited = [node]

    while queue:
        x = queue.pop(0)
        for i in G[x]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    print(visited)
#breathFirstSearch(G, "S")

#Exercise # 4a ------------->
def nodes_of_level(G, level, start = 0):
    check, queue, levels = [False]*len(G), [start], [0]*len(G)
    while queue:
        x = queue.pop()
        if check[x] == False:
            check[x] = True
            for y in G[x]:
                if check[y] == False:
                    levels[y] = levels[x] + 1
                    queue.append(y)
    return [i for i in range(len(levels)) if levels[i] == level]            
print(nodes_of_level(G, 2))

#Exercise # 4b ----------------->
def get_node_level(G, node, start = 0):
    check, queue, levels = [False]*len(G), [start], [0]*len(G)
    while queue:
        x = queue.pop()
        if check[x] == False:
            check[x] = True
            for y in G[x]:
                if check[y] == False:
                    levels[y] = levels[x] + 1
                    queue.append(y)
    return levels[node]
print(get_node_level(G, 6))