'''Pilas  son estructuras de datos, se simulan pues no estan incluidas en python
Estructura de datos tipo lifo imput first output '''

pila= [1,2,3]

#Agrego elementos por el final
pila.append(4)
pila.append(5)

print(pila)

#Sacando elementos por el final
n= pila.pop()
print(f"Sacando el elemento {n}")

print(pila)

