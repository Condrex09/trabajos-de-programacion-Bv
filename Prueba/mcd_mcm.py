import math

def calcular_mcd(a, b):
    return math.gcd(a, b)

def calcular_mcm(a, b):
    return abs(a * b) // calcular_mcd(a, b)

def interactuar_con_usuario():
    print("calculo de MCD y MCM de dos numeros.")
    try:
        numero1 = int(input("ingrese su primer numero entero: "))
        numero2 = int(input("ingrese su segundo numero entero: "))

        mcd = calcular_mcd(numero1, numero2)
        mcm = calcular_mcm(numero1, numero2)

        print(f"el maximo comun divisor de {numero1} y {numero2} es: {mcd}")
        print(f"el maximo comun multiplo de {numero1} y {numero2} es: {mcm}")
    except ValueError:
        print("ingrese solo numeros enteros validos.")
interactuar_con_usuario()