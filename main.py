import picklelib # library for pickle handling
import network # library for the network usage
import DVR_node # library for the node abstraction
# import djstra # library for djistra link state routing
import json
import sys
import time

net_structure = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 4},
    'C': {'A': 3},
    'D': {'B': 4}
}

user_pwd = {
        'pepa_A': 'pepapls1',
        'pepa_B': 'pepapls2',
        'pepa_C': 'pepapls3',
        'pepa_D': 'pepapls4'
}

# save the net structure so it can be loaded easily
picklelib.save_pickle('structure.pickle', net_structure)
picklelib.save_pickle('user_pwd.pickle', user_pwd)

# load the net structure for test
net_structure = picklelib.get_pickle_info('structure.pickle')
user_pwd = picklelib.get_pickle_info('user_pwd.pickle')

# ----------------------------------- ya el programa ----------------------------------------- #

# for each fo the values in the user dictionary create a network class instance

def menu():
    for i in user_pwd:
        print("Press "+ i[5:6] + " Use: " + i + " Node: " + str(i[5:6]))
    return 0

def destino(home):
    for i in user_pwd:
        if home != str(i[5:6]):
            print("Press "+ i[5:6] + " To message " + str(i[5:6]))
    return 0


menu()
value = input()  
HOME_NODE = value.upper()
DVR_HOME_NODE = DVR_node.DVR_node(HOME_NODE)

try:
    USERNAME = 'pepa_'+HOME_NODE
    PASSWORD = user_pwd[USERNAME]
except:
    print("INVALID LETTER")
    sys.exit()

# do the chat stuff
# register to net
network = network.myBot(USERNAME+'@alumchat.xyz', PASSWORD)
network.register_plugin('xep_0030') # Service Discovery        
network.register_plugin('xep_0004') # Data forms
network.register_plugin('xep_0066') # Out-of-band Data
network.register_plugin('xep_0077') # In-band Registration FORCED
network.register_plugin('xep_0199') # network Ping
network.register_plugin('xep_0045') # Annotations


if network.connect(("alumchat.xyz", 5222)):
    print("CONNECTED TO SERVER")
    network.process()
                    
else:
    print("COULD NOT CONNECT TO SERVER")    

# create a DVR node instance

# create a new dictionary with the known paths and costs
for node in net_structure[HOME_NODE]:
    DVR_HOME_NODE.add_distances(node, net_structure[HOME_NODE][node])

    # add the requested nodes to list of visited
    DVR_HOME_NODE.add_visited(node, net_structure[HOME_NODE][node])


time.sleep(6)

while(True):
    destino(HOME_NODE)
    obj = input().upper()
    # design a custom message that we can parse later
    message_dict = {
            "n_fuente": HOME_NODE,
            "n_destino": obj,
            "saltos": 0,
            "distancia": 0,
            "lista_nodos": 0,
            "mensaje": "welp"
        }
    message = json.dumps(message_dict)
    # iterate over the known visited nodes and send them a message to the objective 
    for target in DVR_HOME_NODE.visited:
        if HOME_NODE != target:
            network.send_message(mto='pepa_'+target+'@alumchat.xyz', mbody = message, mtype = 'chat')