'''Colas
Estructura de datos de tipo fifo first imput first output
Deben ser simuladas

Se puede utilizar el modulo colection
metodo alternatico
'''

cola = ["maria","jose","alejandro"]

#Agregamos elementos al final
cola.append("Karla")
cola.append("Flor")

print(cola)

#Sacando elementos por el principio de la cola

n=cola.pop(0)
print(f"Atendieron a {n}")

print(cola)
n=cola.pop(0)
print(f"Atendieron a {n}")
