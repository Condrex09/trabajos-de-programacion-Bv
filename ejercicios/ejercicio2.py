# lista_peliculas = ["Destino Final","Eternauta","Lilo y Stich","Los piratas del caribe","el bueno, el malo y el feo"]

# print(lista_peliculas[0])
# print(lista_peliculas[1])
# print(lista_peliculas[2])
# print(lista_peliculas[3])

# contador = 1
# for pelicula in lista_peliculas:
#     print(f"{contador}.-{pelicula}")
#     contador = contador + 1

# for i in range(len(lista_peliculas)):
#     print(f"{i}.-{lista_peliculas[i]}")
# print()
# print(lista_peliculas[2])
# print(f"3.:{lista_peliculas[2]}")

lista_estudiantes = [
    ["Aquiles Baeza",[6.5,5.7,6.3]],
    ["Wendy Sulca",[5.0,4.7,5.8]],
    ["Peter Parker",[7.0,6.8,7.0]],
    ["Delfin Quispe",[4.3,3.8,2.9]]
]

# for x in range(len(lista_estudiantes)):
#     print(f"{x}.-{lista_estudiantes[x]}")
# print()
# contador = 1
# for estudiantes in lista_estudiantes:
#     print(f"{contador}.-{estudiantes}")
#     contador = contador + 1

# for x in range(len(lista_estudiantes)):
#     for n in range(len(lista_estudiantes[x])):
#         print(lista_estudiantes[x][n])

# for estudiante in lista_estudiantes:
#     print(estudiante[0])
    # for i in range(len(estudiante)):
    #     print(estudiante[0])

for estudiante in lista_estudiantes:
    suma = 0
    for i in range(len(estudiante[1])):
        suma = suma + estudiante[1][i]
    promedio = suma / len(estudiante[1])
    print(f"{estudiante[0]}, Notas:{estudiante[1]}, Promedio:{round(promedio,1)}")
    print()

print(len("DOTA"))
print(len(range(10)))
