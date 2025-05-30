#Sala de juegos...
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("debe pagar $10.000 por la entrada.")
elif edad >= 4:
    print("debe pagar $5000.")
elif edad <= 4:
    print("puede entrar gratis.")

