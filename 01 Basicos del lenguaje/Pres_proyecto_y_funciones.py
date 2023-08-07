#
clientes = 'pablo, ricardo,'
#Punto de entrada 
if __name__ == '__main__':
    clientes += 'david,'
    clientes += 'Henrry'
    print(clientes)
    
#Funciones
#La funcion es una secuencia(statements, son ouputs) enunciados, con nombre que realizan un(computo)una serie de instrucciones
#Tiene nombre, paramentros, y valor de salida o regreso
# Tiene libreria estandar con muchas funciones

def suma_de_dos_numeros(x,y):
    return x+y

print ("La suma de dos nujeros en una funcion es:" ,suma_de_dos_numeros(4,5))
