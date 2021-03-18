#Tuplas listas inmutables (no se pueden modificar)

tupla = (4,"hola",6.6, [4,3,5],1)

print(tupla)
print(tupla[1])
print(4 in tupla)
print(tupla.index("hola"))
print(tupla.count(2))
print(len(tupla))

#transformar tupla en lista

lista= list(tupla)

#transformar lista en tupla

lista1 = [1,2,3,4]

tupla1 = tuple(lista)
