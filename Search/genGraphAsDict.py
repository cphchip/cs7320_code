# TODO: Implement code to generate Python dict from list of tuples generate dict

def build_graph_as_dict(node_list, isDirectedGraph):
    user_dict = {}
    # todo: write code here
    if isDirectedGraph == True:
        user_dict = dict(node_list)

    else:
        user_dict = dict(node_list)

    # print(user_dict) #debug line
    return user_dict

# This portion of the code is for testing only. Delete before submittal
'''
node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]
isDirectedGraph = True
build_graph_as_dict(node_list, isDirectedGraph)
'''