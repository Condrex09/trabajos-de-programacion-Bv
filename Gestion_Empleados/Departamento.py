import Conexion from Conexion
conexion = Conexion()
cur, mydb = conexion.conectar()

class departamento:
    def __init__(self, crear, editar, buscar, eliminar):
        self.crear = crear
        self.editar = editar
        self.buscar = buscar
        self.eliminar = eliminar

    def crear(self):
        curCrear = mydb.cursor()
        nombre = input("Ingrese el nombre del Departamento: ")
        gerente = input("Ingrese el nombre del gerente: ")
        print("Departamento creado exitosamente.")
        cur.execute(f'INSERT INTO departamento (nombre, gerente) VALUES ("{nombre}", "{gerente}")')
        self.mydb.commit()
        print("Departamento creado correctamente")
        curCrear.close()

    def editar_(self):
        curEditar = mydb.cursor()
        codigo = input("ingrese el codigo del departamento para actualizar: ")
        nombre = input("Ingrese el nuevo nombre del departamento: ")
        gerente = input("Ingrese el nuevo nombre del gerente: ")
        curEditar.execute(f'UPDATE departamento SET nombre="{nombre}", gerente="{gerente}" WHERE codigo="{codigo}"')
        self.mydb.commit()
        print("Departamento actualizado correctamente")
        curEditar.close()

    def eliminar(self):
        curEliminar = mydb.cursor()
        codigo = input("Ingrese el codigo del departamento para Eliminar")
        curEliminar.execute(f'DELETE FROM departamento WHERE codigo = "{codigo}"')
        self.mydb.commit()
        print("El Departamento se elimino Correctamente")
        curEliminar.close()
    
    def listar(self):
        curListar = mydb.cursor()
        curListar.execute('SELECT codigo, nombre, gerente FROM departamento')
        resultado = curListar.fetchall()
        for resultado in resultado:
            for fila in resultado:
                print(fila)
        curListar.close()
    
    def buscar(self):
        curBuscar = mydb.cursor()
        codigo = input("Ingrese el código del departamento a buscar: ")
        curBuscar.execute(f'SELECT codigo, nombre, gerente FROM departamento WHERE codigo="{codigo}"')
        resultado = cur.fetchall()
        print("Estos son los Departamentos:")
        if resultado:
            print(f"Departamento encontrado con el Codigo: {resultado[0]}, Nombre: {resultado[1]}, Gerente: {resultado[2]}")
        else:
            print("No se encontro un departamento con ese código.")
        curBuscar.close()
print(departamento)

