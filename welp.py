import picklelib

HOME_NODE = 'A'

net_structure = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 4},
    'C': {'A': 3},
    'D': {'B': 4}
}

# save the net structure so it can be loaded easily
picklelib.save_pickle('structure.pickle', net_structure)

# load the net structure for test
net_structure = picklelib.get_pickle_info('structure.pickle')
print(net_structure)

class DVR_node:

    def __init__(self, node):
        self.homenode = node
        self.nodeslist = [node]
        self.distances = {}
        self.visited ={self.homenode:0} # home node distance is zero always

    def add_visited(self, node, distance):
        self.visited[node] = distance
        return(self.visited)

    def add_nodeslist(self, node):
        self.nodeslist.append(node)
        return(self.nodeslist)

    def add_distances(self, node, distance):
        self.distances[node] = distance
        return(self.distances)

    def modify_distances(self, node, distance):
        self.distances[node] = distance
        return(self.distances)

DVR_HOME_NODE = DVR_node(HOME_NODE)
# add to visited test
print(DVR_HOME_NODE.add_visited('B', 50))
# add nodeslist test
print(DVR_HOME_NODE.add_nodeslist('B'))
# add distances test
print(DVR_HOME_NODE.add_distances('B', 50))
# modify distances test
print(DVR_HOME_NODE.modify_distances('B', 100))

