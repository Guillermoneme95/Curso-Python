#Bucle While

import math

numero = int(input("Digite un numero: "))

while numero<0: #Tambien se maneja con identacion
    print("Ingrese un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")
