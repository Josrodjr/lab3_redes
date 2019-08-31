# Jose Rodolfo Perez 16056
# Cristopher Sebastian Recinos 16005

# used libs
import logging
import sys
import sleekxmpp
from sleekxmpp.exceptions import IqError, IqTimeout
import json
import picklelib

# variables
USER = 'test'
HOST = '@alumchat.xyz'
PASSWORD = 'test'


class myBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password):
        
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.start)

        self.add_event_handler("register", self.register)

        self.add_event_handler('message', self.recv_message)


    def start(self, event):
        print("SENDING PRESENCE")
        # SET RESPONSE TIMER LOW SO WE CAN DEBUG
        self.send_presence()
        self.get_roster()

        try:
            self.get_roster()
        except IqError as err:
            logging.error('There was an error getting the roster')
            logging.error(err.iq['error']['condition'])
            self.disconnect()
        except IqTimeout:
            logging.error('Server is taking too long to respond')
            self.disconnect()
    
    def register(self, iq):
        print("REGISTERING ACCOUNT")

        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            resp.send(now=True)
            logging.info("Account created for %s!" % self.boundjid)
        except IqError as e:
            logging.error("Could not register account: %s" %
                    e.iq['error']['text'])
        except IqTimeout:
            logging.error("No response from server.")
            self.disconnect()

    def message(self, recipient, msg):
        self.message_info = msg
        self.recipient_msg = recipient
        self.send_message(mto=self.recipient_msg, mbody=self.message_info)
    
    def recv_message(self, msg):
        # try and parse to json the message info
        # print(msg['to'])
        try:
            json_info = json.loads(msg['body'])
            # print(json_info['n_fuente'])

            actual_node = json_info['current']
            print("este nodo ",actual_node)

            # get the info for this node from net
            net_structure = picklelib.get_pickle_info('structure.pickle')
            print(net_structure[actual_node])

            # check if any of this nodes neighbor is the node we are looking for
            for neighbor in net_structure[actual_node]:
                # print(neighbor)
                if neighbor != json_info['n_fuente']:
                    # send a modified message searching for the node

                    # check if node already passed here
                    nodes_traveled = [x.strip() for x in json_info['lista_nodos'].split(',')]
                    if neighbor not in nodes_traveled:
                        message_dict = {
                            "n_fuente": json_info['n_fuente'],
                            "current": neighbor,
                            "n_destino": json_info['n_destino'],
                            "saltos": json_info['saltos'] + 1,
                            "distancia": json_info['distancia'] + net_structure[actual_node][neighbor],
                            "lista_nodos": json_info['lista_nodos'] +", "+ actual_node,
                            "mensaje": "welp"
                        }
                        message = json.dumps(message_dict)
                        # send message
                        self.send_message(mto='pepa_'+neighbor+'@alumchat.xyz', mbody = message, mtype = 'chat')
                        # self.send_message(mto='pepa_a@alumchat.xyz', mbody = 'TEST', mtype = 'chat')
            if actual_node == json_info['n_destino']:
                # return a success to the generator
                message_dict = {
                    "n_fuente": json_info['n_destino'],
                    "current": actual_node,
                    "n_destino": json_info['n_fuente'],
                    "saltos": json_info['saltos']*2,
                    "distancia": json_info['distancia'] + net_structure[actual_node][neighbor],
                    "lista_nodos": json_info['lista_nodos'] + actual_node,
                    "mensaje": "COMPLETED"
                }
                message = json.dumps(message_dict) + 'STATUS: COMPLETED'
                # send message
                self.send_message(mto='pepa_'+json_info['n_fuente']+'@alumchat.xyz', mbody = message, mtype = 'chat')
                # print
                print(message)

        except:
            print(str(msg['from']) + ": " + str(msg['subject']) + "\n")
            print(str(msg['body']) + "\n")

    def dissconect(self):
        self.disconnect(wait=True)


def print_menu():
    print("0: CONNECT TO SERVER")
    print("1: SEND MESSAGE")
    print("2: DISCONNECT")


if __name__ == '__main__':
    # hardcoded the info for testing 

    while (True):
        # print menu
        print_menu()
        print("Insert a number")
        option = input()
        try:
            # convert to int and start the switch  
            value=int(option)
            print("SELECTED OPTION: " + option)     
            
            if value == 0:
                # connect and register to server
                print("Enter a username: ")
                USER = input()
                print("Enter a password: ")
                PASSWORD = input()

                xmpp = myBot(USER+HOST, PASSWORD)

                xmpp.register_plugin('xep_0030') # Service Discovery
                xmpp.register_plugin('xep_0004') # Data forms
                xmpp.register_plugin('xep_0066') # Out-of-band Data
                xmpp.register_plugin('xep_0077') # In-band Registration FORCED
                xmpp.register_plugin('xep_0199') # XMPP Ping
                xmpp.register_plugin('xep_0045') # Annotations

                if xmpp.connect(("alumchat.xyz", 5222)):
                    print("CONNECTED TO SERVER")
                    xmpp.process()
                    
                else:
                    print("COULD NOT CONNECT TO SERVER")

            elif value == 1:
                # send a message
                print("Para quien es el mensaje?: ")
                recipient = input()
                print("Texto del mensaje?: ")
                text = input()
                print("SENDING MESSAGE")
                xmpp.send_message(mto=recipient+HOST, mbody = text, mtype = 'chat')
            elif value == 2:
                # disconnect
                print("DISCONNECTING")
                xmpp.disconnect()
                break

            else:
                print("NOT VALID NUMBER, RETRY")

        except ValueError:
            print("INVALID TYPE, PLEASE INSERT AN INTEGER")
