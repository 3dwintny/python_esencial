clients = 'pablo, ricardo,' 
def create_client(cliente_name):
    global clients
    clients+= cliente_name
    _add_comma()
    
def list_client():
    global clients
    print(clients)

def _add_comma():
    global clients
    
    clients+= ','
    
if __name__ =='__main__':
    list_client()
    create_client('David')
    list_client()
