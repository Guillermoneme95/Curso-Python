'''Construir un programa que simule el fucionamiento de una calciladora que puede realizar las cuatro operacicones basicas.
El usuario debe especificar la operacion con la primera letra de dicha operacion.'''

num1= float(input("Digite el primer numero"))
num2= float(input("Digite el segundo numero"))

operacion= input("Digite la operacion:").upper()

if operacion == 'S':
    suma = num1 + num2
    print(f"\nLa suma es {suma}")
elif operacion == 'R':
    resta = num1 - num2
    print(f"\nLa resta es {resta}")
elif operacion == 'M' or operacion == 'P':
    mult = num1 * num2
    print(f"\nEl producto es {mult}")
elif operacion == 'D' or operacion == 'C':
    if num2 != 0:
        div = num1/num2
        print(f"\nLa division es {div:.2f}")
    else:
        print("No se puede dividir en 0")
else:
    print ("Operacion equivocada")
