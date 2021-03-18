'''Ejercicio 2: Hacer un programa que pida 3 numeros y determine cual es el mayor'''

num1= int(input("Ingrese el primer numero"))
num2= int (input("ingrese el segundo numero"))
num3= int (input("Ingrese el tercer numero"))

if num1>num2 and num1> num3:
    print(f"{num1}es el mayor")
elif num2>num1 and num2>num3:
    print(f"{num2}es el mayor")
elif num3>num1 and num3> num2:
    print(f"{num3}es el mayor")
else:
    print("Son todos iguales")