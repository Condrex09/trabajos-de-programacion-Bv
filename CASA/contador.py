import time

print ("=== CONTADOR CRONOMETRO ===")
tipo = input("Quieres un contador progresivo (p) o regresivo (r)? ").lower()

if tipo == "p":
    limite = int(input("¿Hasta que numero quieres contar?: "))
    contador = 0
    while contador <= limite:
        print(f"Tiempo: {contador} segundos")
        time.sleep(1)
        contador +=1
    print("Contador progresivo terminado")

elif tipo == "r":
    contador = int(input("¿Desde que numero quieres comenzar?: "))
    while contador >= 0:
        print(f"Tiempo restante: {contador} segundos")
        time.sleep(1)
        contador -= 1
    print("Tiempo terminado")

else:
    print("Opcion no valida. Debes escribir 'p' o 'r'.")