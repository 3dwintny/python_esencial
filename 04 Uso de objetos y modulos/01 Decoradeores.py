PASSWORD = '12345678'

def passwor_required(func):
    def wrapper():
        password = input('What is your password')
        
        if password == PASSWORD:
            return func()
        else:
            print('The password is incorrect')
    return wrapper

@passwor_required # Nos permite ejecutar logica antes y despues de la funcion, Nos permite condicionalmete a saber si el usuario tiene acceso a esa funcion o no 
def needs_password():
    print('The password is correct')

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)#args, y kwargs, son argumentos. *lista
        return result.upper()
    return wrapper
@upper #
def say_my_name(name):
    return 'Hola,{}'.format(name)

if __name__ == '__main__':
    #needs_password()
    print(say_my_name('Edwin'))