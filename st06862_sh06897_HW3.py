#
# CS 102 (Data Structures & Algorithms)
#   Assignment 03 (Total points: 100)
#
# ---------------------------------------- #
# COVID-19 Patients' Contact Network       #
# ---------------------------------------- #
#
# Background
# ==========
# You and your patient have decided to start a  project to analyze COVID-19
# patients' contact network. Your patient will handle the website creation (they know
# what they are doing, having experience in Web development). However, it is
# up to you to create a data structure that manages the patients' contact network information
# and to implement several procedures that operate on the network.
#
# On a website, data is stored in a database. In your case, however, all
# information comes in a long string of text. Each pair of sentences in the text
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> traveled to <country1>, ..., <countryN>.
#
# Here, connection sentence shows the user meetings to other users and his/her travel visited
#
# For example:
# 
# Usama is connected to Saeed, Aaliya, Mohsin.Usama traveled to Italy, Japan, Korea.
# 
# Note that connection sentence will be separated from the next by only a period (dot). There will
# not be a whitespace or new lines between sentences.
# 
# Your patient records the information in that string based on user activity on 
# the Website and passes it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the various data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g., lists of dictionaries). Choose one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'Usama' in the network. Furthermore, connections are asymmetric
# - if 'Jawad' is connected to 'Babar', it does not necessarily mean that 'Babar' is
# connected to 'Jawad'.
#
# Assignment Description
# ====================---
# Your task is to complete the procedures according to the specifications below. You are encouraged 
# to define any additional helper function/procedure(s) that might assist you in accomplishing
# a task. You are encouraged to test your code using print statements with different
# data samples. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="Usama is connected to Saeed, Aaliya, Mohsin.\
Usama traveled to Italy, Japan, Korea.\
Saeed is connected to Sumaira, Zehra, Samar, Marium.\
Saeed traveled to China, Afghanistan.\
Marium is connected to Mohsin, Kashif, Saeed.\
Marium traveled to Japan, USA, Iran.\
Sumaira is connected to Usama, Zehra.\
Sumaira traveled to Japan, Saudi Arabia.\
Aaliya is connected to Mohsin, Bari, Sameera, Kashif.\
Aaliya traveled to India, USA, Malaysia.\
Mohsin is connected to Usama, Bari, Saeed.\
Mohsin traveled to Iran, Indonesia, Afghanistan.\
Bari is connected to Zehra, Usama, Mohsin.\
Bari traveled to Japan, India, China.\
Zehra is connected to Marium, Samar, Saeed.\
Zehra traveled to Russia, Malaysia, Italy.\
Sameera is connected to Bari, Usama, Samar, Kashif.\
Sameera traveled to Afghanistan, Korea, Russia.\
Kashif is connected to Zehra.\
Kashif traveled to Russia, Malaysia.\
Samar is connected to Sumaira, Usama, Aaliya.\
Samar traveled to Saudi Arabia, Indonesia, Iran."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): [20 Points]
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the information on
#   connections and countries traveled for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A traveled to X, Y, Z.C is connected to A.C traveled to X."
#   as a test case for create_data_structure because the string does not 
#   lists B's connections or traveled countries.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return an empty data structure ('network').
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    people = {}
    places = {}
    lst1, lst2 = [], []
    network = []
    string_input = string_input.replace(" is connected to",",").replace(" traveled to",",").split(".")
    for i in range(len(string_input)):
        if i%2 == 0:
            lst1.append(string_input[i].split(', '))
        else:
            lst2.append(string_input[i].split(', '))
    for j in lst1:
        lst = []
        for k in range(1, len(j)):
            lst.append(j[k])
        people[j[0]] = lst
    
    for j in lst2:
        lst = []
        for k in range(1, len(j)):
            lst.append(j[k])
        places[j[0]] = lst
    network.append(people)
    network.append(places)
    return (network)
net = create_data_structure(example_input)

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is a 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from the 'network'.        #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): [05 Points]
#   Returns a list of all the connections that the user has
#
# Arguments: 
#   network: the patients network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
    #If the user is not in network, return None.
    if not user in network[0]:
        return None
    return network[0][user]

# ----------------------------------------------------------------------------- 
# get_countries_traveled(network, user): [05 Points]
#   Returns a list of all the countries a user traveled.
#
# Arguments: 
#   network: the patients' network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all countries the user traveled.
#   - If the user traveled no countries, return an empty list.
#   - If the user is not in network, return None.
def get_countries_traveled(network, user):
    #If the user is not in network, return None.
    if not user in network[1]:
        return None
    return network[1][user]

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): [05 Points]
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the patients network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, the network remains unchanged.
#   - If user_A or user_B is not in network, return None.
def add_connection(network, user_A, user_B):
    if user_A in network[0] and user_B in network[0]:  
        userA_conn=network[0][user_A]
        if not user_B in userA_conn:
            userA_conn.append(user_B)
        network[0][user_A]=userA_conn
        return network
    else:
        return None

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, countries): [05 Points]
#   Creates a new user profile and adds that user to the network, along with
#   any country traveled specified in countries. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the patients network data structure
#   user:    a string containing the name of the user to be added to the network
#   countries:   a list of strings containing the user's traveled countries, e.g.,
#            ['Indonesia', 'Afghanistan', 'Korea']
#
# Return: 
#   The updated network with the new user and countries traveled added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's traveled countries)
def add_new_user(network, user, countries):
    if user in network[0]:
        return network
    network[0][user]=[]
    network[1][user]=countries
    return network

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): [15 Points]
#   Finds all the secondary connections (i.e., connections of connections) of a
#   given user.
# 
# Arguments: 
#   network: the patients network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if user not in network[0]:
        return None
    if network[0][user]==[]:
        return []
    primary_connections=network[0][user]
    secondary_connections=[]
    for prim_conn in primary_connections:
        for sec_conn in network[0][prim_conn]:
            if not sec_conn in secondary_connections:
                secondary_connections.append(sec_conn)
    return secondary_connections

# -----------------------------------------------------------------------------     
# count_common_connections(network, user_A, user_B): [10 Points]
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the patients network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    common_count=0
    if user_A not in network[0] or user_B not in network[0]:
        return False
    user_A_conn=network[0][user_A]
    user_B_conn=network[0][user_B]
    for i in user_A_conn:
        if i in user_B_conn:
            common_count+=1
    return common_count

# ----------------------------------------------------------------------------- 
# find_find_path_to_patient(network, user_A, user_B): [15 Points]
#   Finds a path  from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample path:
#   >>> print find_find_path_to_patient(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.

#Helper_Function

def find_path_to_patient(network, user_A, user_B, visited=[], path=[]):
    connections = network[0][user_A]
    if connections==[]:
        return None    
    path.append(user_A)
    visited.append(user_A)
    for connection in connections:
        if connection==user_B:
            path.append(connection)
            return path
        elif connection not in visited:
            temp = find_path_to_patient(network, connection, user_B, visited, path)
            if temp != None:
                return path
    path.remove(user_A)
    return None


# ----------------------------------------------------------------------------- 
# find_all_possible_paths_to_user(network, user_A, user_B):  [20 points]
#   Finds all possible path from user_A to user_B.
#  
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A nested list which contains sublist of possible paths from user_A to user_B.
#   - If there exists no path in between the two users, the function will return an empty list.
#   - If user_A or user_B is not in network, return None.
#
# Sample path:
#   >>> find_all_possible_paths_to_user(network, "Abe", "Zed")
#   >>> [['Abe', 'Zed'], ['Abe', 'Tom', 'Zed'], ['Abe', 'Gel', 'Sam', 'Zed']]
#
def find_all_possible_paths_to_user(network, user_A, user_B):
    paths = network[0]
    visited = []
    path = []
    result = []
    if user_A in paths.keys() and user_B in paths.keys():
        dfs(paths, user_A, user_B, visited, path, result)
        return result
    else:
        return None



def dfs(paths, node, target, visited, path, result):
    visited.append(node)
    path.append(node)

    if node == target:
        result.append(path.copy())
    
    else:
        for nx in paths[node]:
            if nx not in visited:
                dfs(paths, nx, target, visited, path, result)
        
    path.pop()
    visited.pop()
#Maam is mn mujh se one list create nhi horhi thi

net = create_data_structure(example_input)
#print(net)
#print(get_connections(net, "Aaliya"))
#print(get_connections(net, "Marium"))
#print(get_countries_traveled(net, "Usama"))
#print(add_connection(net, "Usama", "Samar"))
#print(add_new_user(net, "Aaliya", []))
#print(add_new_user(net, "Nick", ["India", "Italy"])) # True
#print(get_secondary_connections(net, "Marium"))
#print(count_common_connections(net, "Marium", "Usama"))
#print(find_path_to_patient(net, "Usama", "Zehra"))
#print(find_all_possible_paths_to_user(net, "Usama", "Zehra"))