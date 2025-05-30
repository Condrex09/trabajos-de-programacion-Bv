#Contraseña correcta...
contraseña_correcta = input("Ingrese su nueva contraseña: ")

contraseña = ""

while not contraseña == contraseña_correcta:
    contraseña = input("Escriba la contraseña: ")
    if not contraseña == contraseña_correcta:
        print("incorrecta. intenta de nuevo.")

print("contraseña correcta...")