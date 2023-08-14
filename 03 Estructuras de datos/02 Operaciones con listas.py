#Tipos de operadores con listas
import random
a = [1,2]
b = [3,4]
#suma
print(a+b)
#mulitiplicación
print(a*3)

#Las listas tienen varios metodos que podemos usar 

a = [1]
print(a)
#agregamos un 2 a las listas
a.append(2)
a.append(5)
a.append(3)
print(a)
#Para ordenar una lista , usamos el metodo sort
a.sort()
print(a)
# Para eliminar la ultima fila de una lista usamos el metdo pop
a.pop()
print(a)
#Podemos elimiar
del a[-1]
print(a)
#Remover sin saber, donde esta ubicado el valor que deseamos eliminar
a.remove(2)
print(a)


c = list(range(2,22,2))
print(c*2)


#random 
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,15))
#Lo anterior genera 10 numeros random entre 0 y 15
print(random_numbers)
#No ordenamos la lista inicial
order_numers = sorted(random_numbers)
print(order_numers)
#Ordenamos la lista inical
random_numbers.sort()
print(random_numbers)

# con la funcion dir(nombre de la variable), nos dara los metodos que podemos usar para la variable
print(dir(random_numbers))
