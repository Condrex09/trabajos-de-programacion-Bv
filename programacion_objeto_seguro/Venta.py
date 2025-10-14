#relacionada con un (FK)cliente y un (FK)libro
from Conexion import Conexion

conexion = Conexion()
cur, mydb = conexion.conectar()
    
class Venta:
    def __init__(self, rut, codigo, cantidad, total):
        self.rut = rut
        self.codigo = codigo
        self.cantidad = cantidad
        self.total = total

    def crear_venta(self):
        cur = mydb.cursor()
         # Solicitar los datos de la venta
        self.rut = input("Ingrese el RUT del cliente: ")
        #mostrar los libros disponibles
      

        self.codigo = input("Ingrese el código del libro: ")
        self.cantidad = input("Ingrese la cantidad: ")
        self.total = input("Ingrese el total de la venta: ")

        cur.execute(f'INSERT INTO venta (rut, codigo, cantidad, total) \
                    VALUES ("{self.rut}", "{self.codigo}", {self.cantidad}, {self.total})')
        mydb.commit()

    #traer el nombre del libro y el nombre del cliente
    def consultar_ventas(self):
        cur.execute("SELECT c.nombre, l.titulo, v.total FROM venta v, cliente c, libro l \
                    where c.rut = v.rut")
        resultados = cur.fetchall()
        for fila in resultados:
            print(fila)

    #traer las ventas de un cliente especifico
    def consultar_ventas_cliente(self):
        self.rut = input("Ingrese el RUT del cliente: ")
        cur.execute(f"SELECT c.nombre, l.titulo, v.cantidad, v.total FROM venta v, cliente c, libro l \
                    where c.rut = '{self.rut}'")
        resultados = cur.fetchall()
        for fila in resultados:
            print(fila)

    def menu_venta():
        print("""
        1.Crear venta
        2.Consultar Venta
        3.Consultar Venta cliente""")
        opc= int(input("Ingrese Opcion: "))
        obj_venta = Venta("", "", 0, 0)
        if opc==1:
            obj_venta = crear_venta()
            obj_venta()
        elif opc==2:
            obj_consultar_venta = consultar_venta()
            obj_venta.consultar_ventas()
        elif opc==3:
            obj_consultar_ventas_cliente = consultar_venta_cliente()
            obj_venta.consultar_ventas_cliente()
        

#crear un objeto de la clase Venta
obj_venta = Venta("", "", 0, 0)
obj_venta.consultar_ventas_cliente()
