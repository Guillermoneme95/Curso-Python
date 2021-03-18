#parte2

lista = [1,2,4,5]
lista2 = [10,11,12,10]

lista.append(6) #agrega un elemento al final de la lista

lista.insert(2,3) #agrega el valor 3 en el indice 2

lista.extend([7,8,9]) #Concatena esta lista al final de la original

lista3 = lista + lista2 #Concatena lista con lista 2
#si a lista *2 se copia lo mismo dos veces
print(lista)
print(lista3)
print(3 in lista) #verifica si 3 esta en lista (condicion)
print(lista.index(5))#retorna el indice del valor 5
print(lista2.copy(10))#Cuenta cuantas veces aparece un valor
lista.pop() #elimina el ultimo elemento
lista.pop(3)#elimina el elemento en el indice 3
lista.remove(5)#elimina el valor de 5 sin importar el indice
lista.clear() #elimina toda la lista
lista.reverse()#invierte la lista
lista.sort()#ordena ascententemente
lista.sort(reverse = True) #ordena descendentemente