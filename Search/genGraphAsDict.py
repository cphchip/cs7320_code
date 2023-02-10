# TODO: Implement code to generate Python dict from list of tuples generate dict

def build_graph_as_dict(node_list, isDirectedGraph):
    dict = {}
    # todo: write code here
    if isDirectedGraph == True:
        for i in node_list:
            dict.setdefault(i[0],[]).append(i[1])
    else:
        for i in node_list:
            dict.setdefault(i[0],[]).append(i[1])
            dict.setdefault(i[1],[]).append(i[0])


    print(dict) #debug line
    return dict

# This portion of the code is for testing only. Delete before submittal.
'''
node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]
isDirectedGraph = True
global_dict = build_graph_as_dict(node_list, isDirectedGraph)

assert ('A' in global_dict.keys()) == True
assert ('B' in global_dict.keys()) == True
assert ('C' in global_dict.keys()) == True

# Test expected number of keys in graph_dict
assert len(global_dict) == 3

# test that we have correct children for 'C'
child_list = global_dict['C']
assert ('D' in child_list) == True
assert ('E' in child_list) == True


# This section tests the undirected graph. Delete before submittal.
node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]
isDeirectedGraph = False
global_dict = build_graph_as_dict(node_list, isDirectedGraph=False)

# test that a key exists for each of the first nodes in node_list tuples (from->to)
assert ('B' in global_dict.keys()) == True
assert ('C' in global_dict.keys()) == True
assert ('A' in global_dict.keys()) == True
assert ('D' in global_dict.keys()) == True
assert ('E' in global_dict.keys()) == True
assert ('F' in global_dict.keys()) == True

# Test expected number of keys in graph_dict
assert len(global_dict)  == 6

# test that we have correct children for 'C'
child_list = global_dict['C']
assert ('D' in child_list) == True
assert ('E' in child_list) == True
assert ('B' in child_list) == True

# test that we have correct children for 'F'
child_list = global_dict['F']
assert ('B' in child_list) == True
'''