import calculadora

while True:
    numero_1 = float(input("ingrese su primer numero: "))
    numero_2 = float(input("ingrese su segundo numero: "))
    operacion = input("ingrese su operacion: ")

    calculadora.calculadora(numero_1, numero_2, operacion)

