#conjuntos grupo de elementos desordenados y no pueden haber elementos duplicados, los elementos
#repetidos no son leidos

conjunto = set() #Debo indicar primero con esta funcion para que
                    #el compilador no piense que es un diccionario (para hacer un conjunto vacio)
                    #Si le agrego elementos {a,b,c} no es necesario la funcion set

conjunto = {1,2,3,"hola",4.677} #no puede haber otra coleccion adentro de un conjunto

conjunto.add(5) #se agrega desordenadamente
conjunto.discard("hola") #se elimina Hola
print(1 in conjunto)
print(2  not in conjunto)
conjunto.clear() #Se elimina todo el conjunto

print(conjunto)