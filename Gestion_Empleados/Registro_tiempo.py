import Conexion from Conexion
conexion = Conexion()
cur, mydb = conexion.conectar()

class RegistroTiempo:
    def __init__(self, crear, listar, buscar, editar, eliminar):
        self.crear = crear
        self.editar = editar
        self.buscar = buscar
        self.eliminar = eliminar
        self.listar = listar

    def crear(self):
        curCrear = mydb.cursor()
        id_empleado = input("Ingrese el id del empleado: ")
        id_proyecto = input("Ingrese el id del proyecto: ")
        fecha = input("Ingrese la fecha: ")
        horas = input("Ingrese la cantidad de horas trabajadas: ")
        descripcion = input("Ingrese una breve descripcion de las tareas: ")
        curCrear.execute(f'INSERT INTO registro_tiempo (id_empleado, id_proyecto, fecha, hora, descripcion FROM registro_tiempo) \
                    VALUES ("{id_empleado}", "{id_proyecto}", "{fecha}", "{horas}", "{descripcion}")')
        mydb.commit()
        print("Registro de tiempo creado")
        curCrear.close()

    def listar(self):
        curListar = mydb.cursor()
        curListar.execute('SELECT id, id_empleado, id_proyecto, fecha, horas, descripcion FROM registro_tiempo')
        resultados = curListar.fetchall()
        print("Lista de Registros de Tiempos:")
        for fila in resultados:
            print(f"ID: {fila[0]}, Empleado: {fila[1]}, Proyecto: {fila[2]}, Fecha: {fila[3]}, Horas: {fila[4]}, Descripcion: {fila[5]}")
        curListar.close()
    
    def buscar(self):
        curBuscar = mydb.cursor()
        id_registro = input("Ingrese el id del registro que busca: ")
        curBuscar.execute(f'SELECT id, id_empleado, id_proyecto, fecha, horas, descripcion FROM registro_tiempo WHERE id = "{id_registro}"')
        resultado = curBuscar.fetchone()
        if resultado:
            print(f"Registro encontrado id: {resultado[0]}, Empleado: {resultado[1]}, Proyecto: {resultado[2]}, Fecha: {resultado[3]}, Horas: {resultado[4]}, Descripcion: {resultado[5]}")
        else:
            print("No se encontro un registro con ese id")
        curBuscar.close()
    

    def editar(self):
        curEditar = mydb.cursor()
        id_registro = input("Ingrese el id del registro para actualizar: ")
        horas = input("Ingrese la nueva cantidad de horas: ")
        descripcion = input("Ingrese la nueva descripcion: ")
        curEditar.execute(f'UPDATE registro_tiempo SET horas="{horas}", descripcion="{descripcion}" WHERE id="{id_registro}"')
        mydb.commit()
        print("Registro de tiempo actualizado correctamente")
        curEditar.close()
    
    def eliminar(self):
        curEliminar = mydb.cursor()
        id_registro = input("Ingrese el id del registro para eliminar: ")
        curEliminar.execute(f'DELETE FROM registro_tiempo where id="{id_registro}"')
        curEliminar.mydb.commit()
        print("Registro de tiempo eliminado correctamente")
        curEliminar.close()