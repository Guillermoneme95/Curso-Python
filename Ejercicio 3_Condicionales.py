'''Ejercicio 3: Hacer un programa que pica un caracter e indique si es vocal o no'''

car= input("Ingrese un caracter: ").lower() #Comando que hace minuscula cualquier valor
#tambien es valido car.lower() pero en este caso no modifico la variable pues no la asigno a ninguna variable
#analogamente existe .upper()

if car == 'a' or car == 'e' or car == 'i' or car == 'o' or car == 'u':
    print(f"{car} es vocal")
else:
    print(f"{car} no es vocal")



