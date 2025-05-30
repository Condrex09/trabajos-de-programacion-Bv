edad = int(input("introduce tu edad: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4000
else:
    precio = 10000
print(f"El precio de la entrada es ${precio}")