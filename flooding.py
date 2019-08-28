    def recv_message(self, msg):
        # try and parse to json the message info
        try:
            json_info = json.loads(msg['body'])

            actual_node = json_info['current']
            print("este nodo ",actual_node)

            # get the info for this node from net
            net_structure = picklelib.get_pickle_info('structure.pickle')
            print(net_structure[actual_node])

            # check if the actual node is the destination
            if actual_node == json_info['n_destino']:
                print("llego lol")

            for neighbor in net_structure[actual_node]:
                # forward message
                message_dict = {
                    "n_fuente": json_info['n_fuente'],
                    "current": neighbor,
                    "n_destino": json_info['n_destino'],
                    "saltos": json_info['saltos'] + 1,
                    "distancia": json_info['distancia'] + 1,
                    "lista_nodos": json_info['lista_nodos'] +", "+ actual_node,
                    "mensaje": "welp"
                }
                message = json.dumps(message_dict)
                # send message
                self.send_message(mto='pepa_'+neighbor+'@alumchat.xyz', mbody = message, mtype = 'chat')


        except:
            print(str(msg['from']) + ": " + str(msg['subject']) + "\n")
            print(str(msg['body']) + "\n")
