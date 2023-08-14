# En esta parte se agrego  al proyecto la opcion de actualizar, la parte de este codiog es este 

def update_clients(old_clients_name,new_clients_name):
    global clients
    if old_clients_name in clients:
        clients = clients.replace(old_clients_name , new_clients_name )
    else:
        print('Client already not in the clients\'s list')
