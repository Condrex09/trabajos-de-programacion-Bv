nombre = "Benjamin"
Apellido = "Baraona"
nombre_completo = nombre + " " + Apellido
#nombre y apellido en mayusculas
nombre_mayusculas = nombre.upper()
apellido_mayusculas = Apellido.upper()
#nombre y apellido en minusculas
nombre_minusculas = nombre_mayusculas.lower()
apellido_minusculas = apellido_mayusculas.lower()
#nombre y apellido en titulo
nombre_titulo = nombre.title()
apellido_titulo = Apellido.title()

print(nombre_completo.endswith("a"))

print(f"hola admirable y maravilloso {nombre} {Apellido} {3+4}")
print(f"nombre y apellido en mayusculas: {nombre_mayusculas} {apellido_mayusculas}")
print(f"nombre y apellido en minusculas: {nombre_minusculas} {apellido_minusculas}")
print(f"nombre y apellido en titulo: {nombre_titulo} {apellido_titulo}")