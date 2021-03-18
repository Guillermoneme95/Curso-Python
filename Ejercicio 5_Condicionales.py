'''Hacer un programa que simule un cajero automatico con un saldo inicial de 1000 y tendra el siguiente
menu de opciones:
1 ingresar dinero en la cuenta
2 retirar dinero de la cuenta
3 Mostrar dinero disponible
4 salir
'''

saldo = 1000

print("\t.:MENU:.")
print("1 ingresar dinero en la cuenta")
print("2 retirar dinero de la cuenta")
print("3 Mostrar dinero disponible")
print("4 salir")

opcion= int(input("Digite una opcion de menu"))
print() # da un salto de linea
if opcion == 1:
    extra = float(input("Cuanto dinero desea ingresar a la cuenta-->"))
    saldo += extra
    print(f"Dinero disponible {saldo}")
elif opcion ==2:
    retirar = float(input("Cuanto dinero desea retirar la cuenta-->"))
    if retirar > saldo:
        print("No se puede retirar esa cantidad")
    else:
        saldo -= retirar
        print(f"Dinero disponible {saldo}")
elif opcion ==3:
    print(f"Dinero disponible {saldo}")
elif opcion == 4:
    print("bye")
else:
    print("Error")