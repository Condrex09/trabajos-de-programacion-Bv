#colecciones de datos
#LISTAS, (colecciones ordenadas de datos mutables)
lista = ["Benjamin Baraona", 49, True]
print(lista)
print(type(lista))

print(lista[0])
lista[1] = 19
print(lista)

print([45, 46, 47])
print(type([45, 46, 47]))

#DICCIONARIOS, colecciones ordenadas de pares o elementos mutables
diccionario = {"nombre":"Benjamin Baraona", "edad": 19, 'es_alumno':True} 
print(diccionario)
print(type(diccionario))
print(diccionario['edad'])
diccionario['edad'] = 18
print(diccionario)

#CONJUNTOS, coleccion desdordenada de elementos
conjunto = {"Benjamin Baraona", 19, True}
print(conjunto)
print(type(conjunto))

conjunto.add(45)
print(conjunto)
conjunto.pop()
print(conjunto)
conjunto.pop()
print(conjunto)

#TUPLA, coleccion IMUTABLE de elementos
tupla = ('Benjamin Baraona', 19, True)
print(tupla)
print(type(tupla))

#tupla [2] = 45
#print(tupla[2])