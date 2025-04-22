#Crear un programa que convierta unidades de temperatura
#Celsius, Kelvin o Fahrenheit
#1.- El usuario debera ingresar el valor de T°.
#2.- El usuario debera ingresar escala de T° original.
#3.- El usuario debera ingresar escaña de T° final.
#4.- El sistema debera entregar resultados de conversion.

# de °c a °k => °c + 273.15
# de °k a °c => °k - 273.15

# de °c a °F => (°c * 9/5) + 32
# de °F a °C => (°F -32) * 5/9

#de °F a °K => (°F -32) * 5/9 + 273.15
#de °K a °F => ((°K - 273.15)* 9/5) + 32

def convertidor_temp(temperatura, inicio, fin):
    resultado = 0
    
    if inicio == "K":
        if fin == "C":
            resultado = 0 - 273.15
        elif fin == "F":
             resultado = ((0 -273.15) * 9/5) + 32
        else:
            print("Escala final erronea")
    elif inicio == "C":
        if fin == "K":
            resultado = 0 + 273.15
        elif fin == "F":
            resultado = (0 * 9/5) + 32
        else:
            print("Escala final erronea")
    elif inicio == "F":
        if fin == "C":
            resultado = (0 -32) * 5/9
        elif fin == "K":
            resultado = (0 -32) * 5/9 + 273.15
        else:
            print("escala final erronea")

        print(resultado)
    print(resultado)


temp = float(input("ingrese su temperatura a convertir: "))
escala_inicial = input("indique escala inicial: C, F o k: ").upper()
escala_final = input("indique escala final: C, F o K°: ").upper()

convertidor_temp(temp,escala_inicial,escala_final)

