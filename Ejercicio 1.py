''' Escriba un programa donde tenga una lsta y que a continuacion, elimine
los elementos repetidos, por ultimo mostrar la lista'''

lista = [1,2,3,"Alejandro",2,2,1,"Alejandro",3]
#debemos convertir lista en conjunto y desaparecen los elementos repetidos
'''Alternativa 1
conjunto= set(lista)
lista = list(conjunto)

#Se imprimira desordenado
'''
lista= list(set(lista))
print(lista)