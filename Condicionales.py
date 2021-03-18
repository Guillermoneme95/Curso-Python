'''
Condicionales
    Sirven para comparar dos resultados y devuelven valores booleanos

'''

numero = int (input("Digite un numero"))

if numero >0:
    print("el numero es positivo") #Todo lo que tenga la misma identacion(tab) pertenece al if
elif numero == 0:
    print("el numero es cero")
else:
    print("el numero es negativo")

print("fin del programa")