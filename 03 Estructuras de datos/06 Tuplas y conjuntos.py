#Tuplas y conjutos

#son simlares a la lista
#la diferencia es que son inmutables, quiere decir que no pueden ser modificadas
# set los conjuntos, no permite elementos duplicados

a = set([1,2,3])
b = set([3,4,5])

b.remove(4)
print(b)
a.add(4)
print(a)