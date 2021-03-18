'''Escriba un programa que tenga dos listas y que a continuacion, cree las siguientes listas
(en las que no debe haber elementos repetidos)

-Lista de elementos que aparecen en las dos listas
-Lista de elementos que aparecen en la primera lista pero no en la segunda
-Lista de elementos que aparecen en la segunda lista pero no en la primera
-Lista de elementos que aparecen en ambas listas
'''

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]
print(f"La primera lista {lista1}")
print(f"La segunda lista {lista2}")
#Elimino elementos repetidos

a = set(lista1)
b = set(lista2)

#Elementos que aparecen en las dos listas

union= list(a | b)
print(f"Lista de elementos que aparecen en las dos listas {union}")
#elementos que aparecen en la primera lista pero  no en la segunda

soloA= list(a-b)
print(f"Lista de elementos que aparecen en la primera lista pero no en la segunda{soloA}")

#elementos que aparecen en la segunda lista pero no en la primera

soloB = list(b-a)
print(f"Lista de elementos que aparecen en la segunda lista pero no en la primera {soloB}")

#elementos que aparecen en ambas listas

interseccion= list(a & b)
print(f"Lista de elementos que aparecen en ambas listas {interseccion}")