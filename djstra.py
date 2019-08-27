import DVR_node
import picklelib

HOME_NODE = 'A'

DVR_HOME_NODE = DVR_node.DVR_node(HOME_NODE)

# get ONLY the info we need for this node
net_structure = picklelib.get_pickle_info('structure.pickle')
# create a new dictionary with the known paths and costs
for node in net_structure[HOME_NODE]:
    DVR_HOME_NODE.add_distances(node, net_structure[HOME_NODE][node])

    # add the requested nodes to list of visited
    DVR_HOME_NODE.add_visited(node, net_structure[HOME_NODE][node])

# request each known node for neighbors and their distances
for node in DVR_HOME_NODE.visited:
    # REQUEST



    # ADD THE REQUESTED ITEMS TO OUR LIST (dummy bcuz same info for now)


    response_data = net_structure[node]
    # add the requested data to our path
    for node_response in response_data:
        # no use for home data for now
        if node_response != HOME_NODE:
            # add distance plus the node it passed over
            DVR_HOME_NODE.add_distances(node_response, response_data[node_response] + DVR_HOME_NODE.visited[node])

# add the requested nodes to list of visited
for node in DVR_HOME_NODE.distances:
    if node != HOME_NODE:
        DVR_HOME_NODE.add_visited(node, DVR_HOME_NODE.distances[node])

print(DVR_HOME_NODE.distances)
