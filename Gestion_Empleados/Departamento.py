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
        curCrear.execute(f'INSERT INTO departamento (nombre, gerente) VALUES ("{nombre}", "{gerente}")')
        mydb.commit()
        print("Departamento creado correctamente")
        curCrear.close()

    def editar_(self):
        curEditar = mydb.cursor()
        codigo_departamento = input("ingrese el codigo_departamento del departamento para actualizar: ")
        nombre = input("Ingrese el nuevo nombre del departamento: ")
        gerente = input("Ingrese el nuevo nombre del gerente: ")
        curEditar.execute(f'UPDATE departamento SET nombre="{nombre}", gerente="{gerente}" WHERE codigo_departamento="{codigo_departamento}"')
        mydb.commit()
        print("Departamento actualizado correctamente")
        curEditar.close()

    def eliminar(self):
        curEliminar = mydb.cursor()
        codigo_departamento = input("Ingrese el codigo_departamento del departamento para Eliminar")
        curEliminar.execute(f'DELETE FROM departamento WHERE codigo_departamento = "{codigo_departamento}"')
        mydb.commit()
        print("El Departamento se elimino Correctamente")
        curEliminar.close()
    
    def listar(self):
        curListar = mydb.cursor()
        curListar.execute('SELECT codigo_departamento, nombre, gerente FROM departamento')
        resultado = curListar.fetchall()
        for resultado in resultado:
            for fila in resultado:
                print(fila)
        curListar.close()
    
    def buscar(self):
        curBuscar = mydb.cursor()
        codigo_departamento = input("Ingrese el código del departamento a buscar: ")
        curBuscar.execute(f'SELECT codigo_departamento, nombre, gerente FROM departamento WHERE codigo_departamento="{codigo_departamento}"')
        resultado = curBuscar.fetchall()
        print("Estos son los Departamentos:")
        if resultado:
            print(f"Departamento encontrado con el Codigo_departamento: {resultado[0]}, Nombre: {resultado[1]}, Gerente: {resultado[2]}")
        else:
            print("No se encontro un departamento con ese código.")
        curBuscar.close()
print(departamento)

