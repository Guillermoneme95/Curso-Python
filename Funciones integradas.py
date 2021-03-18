#Funciones integradas

'''Se pueden convertir cadenas a float o a int agregandole a la variable de la siguiente manera'''

n = int("10") #Todo lo que se encuentre entre " se considera str
m =float ("10.9")

print(type(n))
print(type(m))
print(type("10"))

#Tambien se puede hacer una cadena un valor numerico
n = str(10)
m = str(10.9)

#Convertir entero en binario

l= bin(10)
print(l)
#Convertir entero a exadecimal
f=hex(10)
print (f)
#convertir cualquier valor a enter
i = int ("0b1010",2) #se debe indicar la base del numero a convertir
print(i)
k = int("0xa",16)
print (k)

#Valor absoluto de un numero
w =abs (-8)
print (w)
#redondeado de un numero
r= round(5.6) # redondea al valor mas cercano
print (r)
#Contar caracteres de una cadena
cantidad = len("Hola!")
