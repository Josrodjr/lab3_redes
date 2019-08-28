instanced = []
# instanced_node = []
# instanced_names = []

# for value in user_pwd:
#     # instance
#     print('name '+ value, 'pwd ' + user_pwd[value])
#     # before connect also create node implementation
#     x = str(value[5:6])
#     instanced_names.append(x)
#     node_value = DVR_node.DVR_node(x)
#     instanced_node.append(node_value)
#     # register to net
#     value = network.myBot(value+'@alumchat.xyz', user_pwd[value])
#     value.register_plugin('xep_0030') # Service Discovery        
#     value.register_plugin('xep_0004') # Data forms
#     value.register_plugin('xep_0066') # Out-of-band Data
#     value.register_plugin('xep_0077') # In-band Registration FORCED
#     value.register_plugin('xep_0199') # value Ping
#     value.register_plugin('xep_0045') # Annotations

#     # before connect also create node implementation
#     # node_value = DVR_node.DVR_node(value[4:5])
#     # instanced_node.append(node_value)

#     if value.connect(("alumchat.xyz", 5222)):
#         print("CONNECTED TO SERVER")
#         value.process()
                    
#     else:
#         print("COULD NOT CONNECT TO SERVER")    

#     instanced.append(value)

# # try and send a message to a previously registered user found in user_pwd

# # for value in instanced_node:
#     # print(value)
#     # value.send_message(mto='pepa_A'+'@alumchat.xyz', mbody = 'test', mtype = 'chat')

# # start with fist item
# i = 0
# for value in instanced:
#     # set the default values to the node class
#     for node in net_structure[instanced_names[i]]:
#         instanced_node[i].add_distances(node, net_structure[instanced_names[i]][node])

#         # add the requested nodes to list of visited
#         instanced_node[i].add_visited(node, net_structure[instanced_names[i]][node])
    
#     i += 1 

# j = 0
# for value in instanced:
#     # for each of the instanced canolly ask the neighbors for routes
#     for node in instanced_node[j].visited:
#         # formulate the json
#         x = {
#             "n_fuente": instanced_names[j],
#             "n_destino": node,
#             "saltos": 0,
#             "distancia": 0,
#             "lista_nodos": 0,
#             "mensaje": "welp"
#         }
#         y = json.dumps(x)
#         print(y)
#         # value.send_message('pepa_'+node+'@alumchat.xyz', )
#     j += 1
