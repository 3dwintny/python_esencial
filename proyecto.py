import sys
clients = [
    {
        'name':'pablo',
        'company':'Google',
        'email':'pablo@google.com',
        'position':'Sofrware engineer',        
    },
    {
        'name':'Ricardo',
        'company':'Facebook',
        'email':'ricardo@faceboo.com',
        'position':'Data engineer',
    }
    ]

def serch_client(client_name):
    global clients 
    
    for client in clients:
        if  client_name['name'] in client['name'] :
            return True
        else:
          continue

def delte_client(client_name):
    global clients
    for client in clients:
        if client_name['name'] in client['name']:
            clients.remove(client)
            break
        else:
            print('client is not in client list')

def update_clients(old_clients_name,new_clients_name):
    global clients
    for index, client in enumerate(clients):
        if  old_clients_name['name'] in client['name']:
            clients[index] = new_clients_name
            break
        else:
            print('Client already not in the clients\'s list')

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')

def list_client():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx, 
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position'],
        ))

def _get_client_name():
    client_name = None 
    while not client_name:
        client_name = input('Wat is the client name? \n')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return  client_name

def _get_client_field(field_name):
    field = None
    
    while not field:
        field = input('What is the client {}?  '.format(field_name))
    return field
        
def _print_welcome():
    print('WELCOME TO SALES CODERS')
    print('*'*25)
    print('What would you lke todo today?')
    print('[C]reate client')
    print('[L]list client\'s')
    print('[U]date client')
    print('[D]elete client')
    print('[S]erch client')
    print('[E]xit')

if __name__ =='__main__':
    salir = None
    while salir != 'E':
        _print_welcome()
        command = input()
        #Para estar cubierto a cualqueir error convertimos todo a mayuscula
        command = command.upper()

        if command == 'C':
            client = {
                'name': _get_client_field('name'),
                'company': _get_client_field('company'),
                'email': _get_client_field('email'),
                'position': _get_client_field('position'),
            }
            create_client(client)
            list_client()
            
        elif command == 'L':
            list_client()

        elif command == 'D':
            client = {'name' : _get_client_field('name')}
            delte_client(client)
            list_client()

        elif command == 'U':
            new_client = {
                'name': _get_client_field('name'),
                'company': _get_client_field('company'),
                'email': _get_client_field('email'),
                'position': _get_client_field('position'),
            }
            old_client = {
                'name': _get_client_field('name')
            }
            update_clients(old_client,new_client)
            list_client()
            
        elif command == 'S':
            client_name = {'name':_get_client_field('name')}
            found = serch_client(client_name)
            if found:
                print('The client is in the client\'s list')
            else:
                print('The client:{} is not in our client\'s list'.format(client_name))
        elif command == 'E':
            salir = 'E'
            print('Tank you for your visit')
        else:
            print('Invalid command')
