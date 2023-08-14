# Estructuras de datos
# Listas en python, pueden tener cualquier tipo de datos, 
#Listas pueden tener otras listas, a esto le llamamos Matris
#Son conmutables

#Son referenciales, nos indica donde vive en memoria el valor
import copy
my_lista = ['Edwin','Guatemala', 24, 'Olintepeque']
#copiamos la lista y lo guardamos en otra variable
my_lista2 = copy.copy(my_lista)
my_lista[0] = 'Tony'

print(my_lista2)
print(my_lista)

for lista in my_lista:
    print(lista)
