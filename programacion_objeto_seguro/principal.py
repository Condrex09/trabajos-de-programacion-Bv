from Libreria import Libreria
from Cliente import Cliente
from Libro import Libro
from Venta import Venta

class principal:
    def menu_principal():
        obj = principal()
        print("""
        1. Libreria
        2. Cliente
        3. Libro
        4. Venta""")

        opc= int(input("Ingrese Opcion: "))
        if opc== 1:
            obj = Libreria()
            obj.menu_libreria()
        elif opc==2:
            obj = Cliente()
            obj.menu_cliente()
        elif opc==3:
            obj = Libro()
            obj.menu_libro()
        elif opc==4:
            obj = Venta()
            obj.menu_venta()


    #opciones de libro
# Para la entrega debe completar los Menu de cada clase
# y los metodos base(CRUD)
# Metodos Extra
# Calcular el total de la venta en base al precio del libro ingresado
# Calcular el total de clientes
# Traer los datos del libro con stock mas Bajo
# Calcular el total de ventas por cada Cliente
