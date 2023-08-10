clients = 'pablo, ricardo,'

def update_clients(old_clients_name,new_clients_name):
    global clients
    if old_clients_name in clients:
        clients = clients.replace(old_clients_name , new_clients_name )
    else:
        print('Client already not in the clients\'s list')

def create_client(cliente_name):
    global clients
    if cliente_name not in clients:
        clients+= cliente_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')
    
    
def list_client():
    global clients
    print(clients)

def _add_comma():
    global clients
    
    clients+= ','
def _remove_comma():
    global clients
    
    clients-= ','
    
def _get_client_name():
    return input('Wat is the client name? \n')
    
#def _get_update_client_name():
 #U   return input('Wat is the new client name? \n')

def _print_welcome():
    print('WELCOME TO SALES CODERS')
    print('*'*25)
    print('What would you lke todo today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]date client')
if __name__ =='__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        _get_client_name()
        create_client(_get_client_name())
        list_client()
    elif command == 'D':
        pass
    elif command == 'U':
        _get_client_name
        update_clients(_get_client_name(),input('Wat is the new client name? \n'))
        list_client()
    else:
        print('Invalid command') 
