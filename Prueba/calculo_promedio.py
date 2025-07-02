resultados_estudiantes = [
    ['Aquiles Baeza',[4.5,5.7,7.0,5.3]],
    ['Wendy Sulca',[4.3,4.5,5.2,5.3]],
    ['Delfin Quispe',[3.9,4.8,5.5,5.0]],
    ['Armando Casas',[2.8,4.0,5.5,6.1]]
]

for estudiante in resultados_estudiantes:
    suma = 0
    for i in range(len(estudiante[1])):
        suma = suma + estudiante[1][i]
    promedio = suma / len(estudiante[1])
    print(f"{estudiante[0]}, Notas:{estudiante[1]}, Promedio:{round(promedio,1)}")
    print()
