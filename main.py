import picklelib # library for pickle handling
import network # library for the network usage
import DVR_node # library for the node abstraction
# import djstra # library for djistra link state routing

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

instanced = []

for value in user_pwd:
    # instance
    print('name '+ value, 'pwd ' + user_pwd[value])
    value = network.myBot(value+'@alumchat.xyz', user_pwd[value])
    value.register_plugin('xep_0030') # Service Discovery        
    value.register_plugin('xep_0004') # Data forms
    value.register_plugin('xep_0066') # Out-of-band Data
    value.register_plugin('xep_0077') # In-band Registration FORCED
    value.register_plugin('xep_0199') # value Ping
    value.register_plugin('xep_0045') # Annotations

    if value.connect(("alumchat.xyz", 5222)):
        print("CONNECTED TO SERVER")
        value.process()
                    
    else:
        print("COULD NOT CONNECT TO SERVER")    

    instanced.append(value)

# try and send a message to a previously registered user found in user_pwd

for value in instanced:
    # print(value)
    value.send_message(mto='pepa_A'+'@alumchat.xyz', mbody = 'test', mtype = 'chat')