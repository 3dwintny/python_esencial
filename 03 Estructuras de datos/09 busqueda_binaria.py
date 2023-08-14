# Lista ordenada, busqueda binaria
# Ordenar la lista con Sort
import random 
# Con recursion 
def binary_serch(data, target, low, high):
    if low>high:
        return False
    mid = (low + high) // 2
    
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_serch(data, target, low, mid - 1)
    else:
        return binary_serch(data, target, mid+1, high)
# sin recursion 
def binary_serch2(data, target, low, high):
    encontrado = None
    while encontrado != True or encontrado != False:
        if low>high:
            encontrado = False
            return False
        mid = (low + high) // 2
        if target == data[mid]:
            encontrado = True
            return True
        elif target < data[mid]:
            high = mid-1
        elif target > data[mid]:
            low = mid+1    
            

if __name__ == '__main__':
    lista = [random.randint(0,100) for i in range (10)]
    # Ordena el mismo elemento
    lista.sort()
    # print()
    #Crea una nueva lista, sin modificar la lista inical
    #sorted_lista = sorted(lista)
    print(lista)
    target = int(input('What number would you like to find?'))
    found = binary_serch2(lista, target, 0, len(lista)-1)

    print(found)