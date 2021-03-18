#conjuntos 2da parte

#a = set() si los conjuntos inicialmente fueran vacios deberia empezar declarandolos asi
#b = set()

a= {1,2,3}
b= {3,2,1}
d= {3,5,6}
h={1,2,3,4,5,6}
print(a == b) #Verifico la igualdad VERDAD
print(len(a))

#union de conjuntos
c= a | d

print(c)

#interseccion de dos conjuntos

e= a & d
print(e)

#Diferencia , elementos de A que no estan en D
f= a - d
print(f)
#Diferencia simetrica elementos que estan en A y en D pero que no estan en ambos

g= a ^ d
print(g)

#Como ver si un conjunto es sub conjunto de otro(un connjunto esta contenido en otro)
print(a.issubset(h))
print(b.issubset(h))

#Si estan todos los elementos
print(a.issuperset(h))
#conjuntos disconexos (no comparten elementos)
print(a.isdisjoint(h))
#conjuntos inmutables
j= frozenset({7,8,9})  #no se pueden agregar valores ni borrar elementos