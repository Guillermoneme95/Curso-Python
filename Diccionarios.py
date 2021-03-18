#Diccionarios los elementos se guardan desordenados y tienen dos elementos por posicion
# cada elemento tiene dos elementos  clave y valor; no pueden haber 2 claves iguales

#diccionario = {} diccionario vacio

diccionario = {"azul":"blue","rojo":"red","verde":"green"} #clave:valor
print(diccionario)

#mostrar solo azul
print(diccionario["azul"])

#agregar elementos al diccionario

diccionario["amarillo"]= "yellow"

print(diccionario)

#Eliminar un elemento del diccionario

del(diccionario["verde"])
print(diccionario)

#Puedo poner otro tipo de variables e incluso otras colecciones

dic ={"Willy":["apellido":"Neme Simonetti","estatura":1.76,"edad":23],"Tapir":["N.s",1.83,23]} #tambien podria poner tuplas
#tambien podria poner otro diccionario
print(dic)
