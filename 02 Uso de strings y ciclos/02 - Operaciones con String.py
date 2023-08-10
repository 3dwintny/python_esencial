#upper comvierte todos en mayusculas
#lower todoes en minuscula
#find Encuenta el indice, donde existe un patron que nosotros definimos
#starswith Inicia con un patron
#endswith Termina con un patron
#capitalize Inica con una mayuscula y el resto es minuscula 

#in Se encuenta
#not in  No se encuentra

#Realizando pruebas

country = 'Guatemala'
if 'Guatemala' in country:
    print(country.upper())
if 'Xela' not in country:
    print(country.lower())
print(country.find('t'))
print(country.startswith('Gu'))
print(country.endswith('la'))
print(country.capitalize())