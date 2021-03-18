#Condicionales combinados

edad = int(input("digite su edad:"))


if 0<edad<100: #alternativa edad >0 and edad < 100:
    print("Edad correcta")
    if edad>=18: #condicional anidado
        print("Es mayor de edad")
else:
    print("Edad incorrecta")
