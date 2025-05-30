#Puntuacion
puntuacion = float(input("Introduce su puntuacion (0.0, 0.4, 0.6 o mas): "))

if puntuacion == 0.0:
    nivel = "inaceptable"
elif puntuacion == 0.4:
    nivel = "aceptable"
elif puntuacion >= 0.6:
    nivel = "aceptable"
else:
    nivel = None

if nivel:
    dinero = 250000 * puntuacion
    print(f"Tu nivel de rendimiento es {nivel}")
    print(f"Cantidad de dinero extra: ${dinero:,.2f}")
else:
    print("Tu puntiacion no es valida, debe ser 0.0, 0.4, 0.6 o mas.")