#funcion: set de instrucciones que ejecuta una tarea especifica
#arg: argumentos con los que va a trabajar la función

#definir funcion saludar
def saludar(nombre):
    print(f"Que pasha tio joder ostias te gusta deftones? {nombre}")
nombre = input ("ingrese su nombre: ")

#ejecutar funcion
saludar(nombre)

#Función que sume dos numeros

#DEFINIR FUNCION
def suma(a,b):
    resultado = a + b
    print(f"el resultado de sumar {a} + {b} = {resultado}")
#DEFINIR VARIABLES
numero_1 = int(input("ingrese su primer numero: "))
numero_2 = int(input("ingrese su segundo numero: "))
#EJECUTAR FUNCION
suma(numero_1, numero_2)

#FUNCION QUE HAGA CUALQUIER OPERACION
numero_1 = int(input("ingrese su primer numero: "))
numero_2 = int(input("ingrese su segundo numero: "))
operacion = (input("ingrese su operacion: "))

#DEFINIR FUNCION
def calculadora (a,b,op):
#DEFINIR RESULTADO
    resultado = 0
#CREAR UN CONDICIONAL CON LAS DISTINTAS OPERACIONES
    if op == "+":
        resultado = a + b
    elif op == "*":
        resultado = a * b
    elif op == "-":
        resultado = a - b
    else:
        if numero_2 == 0:
            print("operacion indefinida")
        else:
            resultado = a / b 
    print(f"el resultado de {a}{op}{b} = {resultado}")
#EJECUTAR LA FUNCION
calculadora(numero_1, numero_2, operacion)

lado = float(input("ingrese la medida de su lado: "))

def area_cuadrado(a):
    print(f"el area de su cuadrado de lado {a} = {a*a}")

area_cuadrado(lado)








