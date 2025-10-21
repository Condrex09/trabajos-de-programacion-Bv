import Conexion from Conexion
conexion = Conexion()
cur, mydb = conexion.conectar()

class departamento:
    def __init__(self, nombre, codigo, crear, editar, buscar, eliminar, direccion):
        self.nombre = nombre
        self.codigo = codigo
        self.crear = crear
        self.editar = editar
        self.buscar = buscar
        self.eliminar = eliminar

    def crear(self):
        self.nombre = input("Ingrese el nombre del Departamento: ")
        self.direccion = input("Ingrese la dirección del Departamento: ")
        print("Departamento creado exitosamente.")
        cur.execute(f'INSERT INTO departamento (nombre, direccion) \
                    VALUES ("{self.nombre}", "{self.direccion}")')

    def editar_(self):
        curEditar = mydb.cursor()
        codigo = input("ingrese el codigo del departamento para actualizar")
        nombre = input("Ingrese el nuevo nombre del departamento")
        curEditar.execute(f'UPDATE departamento SET nombre="{nombre}" WHERE codigo = "{codigo}"')
        mydb.commit()

    def eliminar(self):
        curEliminar = mydb.cursor()
        codigo = input("Ingrese el codigo del departamento para Eliminar")
        curEliminar.execute(f'DELETE FROM departamento WHERE codigo = "{codigo}')
        print("El Departamento se elimino Correctamente")
    
    def listar(self):
        curListar = mydb.cursor()
        curListar.execute('SELECT * FROM departamento')
        resultado = curListar.fetchall()
        for resultado in resultado:
            for fila in resultado:
                print(fila)
    
    def buscar(self):
        print(f"Nombre del Departamento: {self.nombre}")
        print(f"Dirección: {self.direccion}")


    def menu_departamento(self):
        print("""Seleccione una opcion para gestionar el departamento
        1. Crear
        2. Editar
        3. Buscar
        4. Eliminar""")
        opc = int(input(""))
        if opc==1:
            print("Crear Departamento")
            obj_crear.crear()
        elif opc==2:
            print("Editar Departamento")
            obj_editar.editar()
        elif opc==3:
            print("Buscar Departamento")
            obj_buscar.buscar()
        elif opc==4:
            print("Eliminar Departamento")
            obj_eliminar.eliminar


