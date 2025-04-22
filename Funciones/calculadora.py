
def calculadora (a,b,op):
    resultado = 0
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