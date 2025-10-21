from Conexion import Conexion

conexion = Conexion()
cur, mydb = conexion.conectar()
class Libreria:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
    
    def mostrar_info(self):
        print(f"Nombre de la librería: {self.nombre}")
        print(f"Dirección: {self.direccion}")

    def crear_libreria(self):
        self.nombre = input("Ingrese el nombre de la librería: ")
        self.direccion = input("Ingrese la dirección de la librería: ")
        print("Librería creada exitosamente.")
        cur.execute(f'INSERT INTO libreria (nombre, direccion) \
                    VALUES ("{self.nombre}", "{self.direccion}")')
        
    def menu_libreria():
        pass