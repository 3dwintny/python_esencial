# estos son los operadores que podemos tener en python
# +, -, /, //, %, *, **
#Podemos ver el tipo de datos
tipo1 = {type("Hola como estas")},{type(5)},{type(5.5)},{type(True)}, {type(3+ 5j)}, {type([3,2,1])} 

for tipo in tipo1:
    print("Con type, sabemos el tipo de dato, por ejemplo",tipo)
    
num1 = 2
num2 = 3

res = num1*num2
print("El resultado es:",res)
    
#Variable
# Variables de una asignacion
message = "como estas?" 
_age = 24 #Variabe privada, cuando tiene un guion vajo antes de el nombre
PI  = 3.12159 # en mayuscula, es probable que no debemos agregar una reasignacion.
__do_not_touch = "Esta variable es importante para el programa, porfavor no modificarla" #Variables que no deben ser modificadas.
#variables que se pueden reasignacion

var_1= 5
var_1= var_1+5
print(var_1)
 
#Expreciones y enunciados
#Expreciones Son instrucciones para el interprete, para que evalue la exprecion
#enununciados, son los resultados de nuestro programa

#Orden de operaciones:
#Parentesis
    #Exponentes
        #Multiplicacion
        #Division
            #Adicion
            #Subtraccion
#PEMDAS Acronimo del orden de las operaciones.
#Variable incorrectas : 43var = 34, global = 34



