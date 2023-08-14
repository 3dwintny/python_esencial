# Estructura de datos en diccionarios

rae = {'Edwin':'Estudiante de ingeniera'}
rae['pizza'] = 'Comida mas deliciosa del mundo'
rae['pasta'] = 'Comida mas delicioasa de italia'

print(rae)

a = rae.get('pizza',None)
b = rae.get('Hola',None)

print(a,"  ",b)
print(rae.keys())
print(rae.values())
print(rae.items())

for key in rae.keys():
    print(key)
for vl in rae.values():
    print(vl)
for key in rae.items():
    print(key)