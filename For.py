#bucle for Tiene un numero determinado de interacciones
#no necesito iniciar la variable
for i in [2,5,7,4,"Alejandro"]: #Se maneja con identacion
                                #Solo repite la cantidad de elementos que tenga la coleccion
    print(i)                    #Toma el valor de los elementos de la coleccion

diccionario = {"Guillermo":22, "Federico":23,"Tapir":34}
print()#Salto de linea

for clave,valor in diccionario.items():
    print(f"{clave}->{valor}")

#recorrer cadenas

coleccion = "Guillermo"

for i in coleccion:
    print(f"{i}", end="-") #cuando termina no hace salto de linea, separa con -

#verificacion de email

b= False

email = input("\nIngrese una direccion de email")

for i in email:
    if i == '@' and i == '.':
         b = True


if b:
    print("El email es correcto")
else:
    print("Email incorrecto")
