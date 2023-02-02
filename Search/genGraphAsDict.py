# TODO: Implement code to generate Python dict from list of tuples generate dict

def build_graph_as_dict(node_list, isDirectedGraph):
    user_dict = {}
    # todo: write code here
    if isDirectedGraph == True:
        # user_dict = dict(node_list)
        for i in node_list:
            user_dict.setdefault(i[0],[]).append(i[1])
    else:
        for i in node_list:
            user_dict.setdefault(i[0],[]).append(i[1])

    print(user_dict) #debug line
    return user_dict

# This portion of the code is for testing only. Delete before submittal.
'''
node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]
isDirectedGraph = True
global_user_dict = build_graph_as_dict(node_list, isDirectedGraph)

assert ('A' in global_user_dict.keys()) == True
assert ('B' in global_user_dict.keys()) == True
assert ('C' in global_user_dict.keys()) == True

# Test expected number of keys in graph_dict
assert len(global_user_dict) == 3

# test that we have correct children for 'C'
child_list = global_user_dict['C']
assert ('D' in child_list) == True
assert ('E' in child_list) == True
'''

# This section tests the undirected graph. Delete before submittal.
node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]
isDeirectedGraph = False
global_user_dict = build_graph_as_dict(node_list, isDirectedGraph=False)

# test that a key exists for each of the first nodes in node_list tuples (from->to)
assert ('B' in global_user_dict.keys()) == True
assert ('C' in global_user_dict.keys()) == True
assert ('A' in global_user_dict.keys()) == True
assert ('D' in global_user_dict.keys()) == True
assert ('E' in global_user_dict.keys()) == True
assert ('F' in global_user_dict.keys()) == True

# Test expected number of keys in graph_dict
assert len(global_user_dict)  == 6

# test that we have correct children for 'C'
child_list = global_user_dict['C']
assert ('D' in child_list) == True
assert ('E' in child_list) == True
assert ('B' in child_list) == True

# test that we have correct children for 'F'
child_list = global_user_dict['F']
assert ('B' in child_list) == True