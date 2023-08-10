# In spanish is cadenas
# len sabe la longitud del string

country = 'Guatemala'
primary_letter = country[0]
id_memory_promary_letter = id(primary_letter)
print('encontramos el lugar donde esta ubicado en la memoria la primera letra de nuestro pais y es: ',id_memory_promary_letter)

other_var = 'G'

print('Lugar donde se encuentra G', id(other_var))