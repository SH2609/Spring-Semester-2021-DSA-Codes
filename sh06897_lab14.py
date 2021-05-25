#bst = {'value': 8, 'left': {'value': 3, 'left': {'value': 1, 'left': {}, 'right': {}}, 'right': {'value': 6, 'left': {'value': 4, 'left': {}, 'right': {}}, 'right': {'value': 7, 'left': {}, 'right': {}}}}, 'right': {'value': 10, 'left': {}, 'right': {'value': 14, 'left': {'value': 13, 'left': {}, 'right': {}}, 'right': {}}}}

def insert(bst, key):
    if not(bst):
        bst['value'] = key
        bst['left'] = {}
        bst['right'] = {}
        return bst

    root_node = bst['value']

    if key < root_node:
        insert(bst['left'], key)
    else:
        insert(bst['right'], key)

    return bst


def bst_gen(bst, keys):
    for key in keys:
        insert(bst, key)
    return bst

def exist(bst, key):
    if not(bst):
        return False
    if bst['value'] == key:
        return True
    else:
        if bst['value'] < key:
            return exist(bst['right'], key)
        if bst['value'] > key:
            return exist(bst['left'], key)
#print(exist(bst, 23))

def minimum(bst, starting_node):
    null=False
    while not(null):
        if bst['left']:
            bst=bst['left']
            continue
        return bst['value']
#print(minimum(bst, 7))

def maximum(bst, starting_node):
	null=False
	while null==False:
		if bst['right']!={}:
			bst=bst['right']
			continue
		return bst['value']
#print(maximum(bst, 3))

#Question 1

#a) Using the helper function insert (bst, key), create the binary search tree that results from inserting the
#following keys in the order given: 68, 88, 61, 89, 94, 50, 4, 76, 66, and 82.
bst = bst_gen({}, [68, 88, 61, 89, 94, 50, 4, 76, 66, 82])
print(bst)

#b) Using the helper function exist (bst, key), check whether key 50 exists in resultant Binary Search Tree.
print(exist(bst,50))
#c) Using the helper function exist (bst, key), check whether key 49 exists in resultant Binary Search Tree.
print(exist(bst,49))
#d) Using the helper function minimum (bst, starting_node), find the node 
#with the minimum value in resultant Binary Search Tree from starting node = 68.
print(minimum(bst, 68))
#e) Using the helper function minimum (bst, starting_node), find the node 
#with the minimum value in resultant Binary Search Tree from starting node = 88.
print(minimum(bst, 88))
#f) Using the helper function maximum (bst, starting_node), find the node 
#with the maximum value in resultant Binary Search Tree from starting node = 68.
print(maximum(bst, 68))
#g) Using the helper function maximum (bst, starting_node), find the node 
#with the maximum value in resultant Binary Search Tree from starting node = 61.
print(maximum(bst, 61))
