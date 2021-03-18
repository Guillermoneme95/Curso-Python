#Diccionario 2

equipo = {10: "Dybala",11:"Costa",7:"Ronaldo"}

print(equipo.get(2,"No existe un jugador con ese dorsal"))#con el get evito el key error equipo[2]

print(10 in equipo)


#imprimir todas las claves
print(equipo.keys())
#imprimir nombres
print(equipo.values())
#impirmir clave y valor ##2
print(equipo.items())
#cuantos elemento hay
print(len(equipo))
#borrar elementos
print(equipo.clear())