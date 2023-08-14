# Son constructos que nos permiten genera secuencias a partir de otas secuencias
import random
lista_de_numeros = list(range(50))
print(lista_de_numeros)

pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print(pares)

student_uid = [1,2,3]
students  = ['Juan', 'Jose', 'Larsen']
# Unimos cada estudiante con su id
students_whit_uid = {uid:student for uid, student in  zip(student_uid, students)}

print(students_whit_uid)
#Creamos una lista de 10 numeros random de dentro de 1 y 3
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,3))
# Genera una lista de numeros no repetidods
non_repeated = { number for number in random_numbers}

print(random_numbers)
print(non_repeated)