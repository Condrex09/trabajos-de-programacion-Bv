import Conexion from Conexion
conexion = Conexion()
cur, mydb = conexion.conectar()

class AsignacionProyecto:
    def __init__(self, AsignarEmpleadoProyecto, EliminarAsignacion, ListarEmpleadosProyecto):
        self.AsignarEmpleadoProyecto = AsignarEmpleadoProyecto
        self.EliminarAsignacion = EliminarAsignacion
        self.ListarEmpleadosProyecto = ListarEmpleadosProyecto

    def asignar_empleado_proyecto(self):
        curAsignarEmpleadoProyecto = mydb.cursor()
        id_empleado = input("Ingrese el id del empleado: ")
        id_proyecto = input("Ingrese el id del proyecto: ")
        curAsignarEmpleadoProyecto.execute(f'INSERT INTO empleado_proyecto (id_empleado, id_proyecto) VALUES ("{id_empleado}", "{id_proyecto}")')
        mydb.commit()
        print("Empleado asignado correctamente al proyecto")
        curAsignarEmpleadoProyecto.close()

    def eliminar_asignacion(self):
        curEliminarAsignacion = mydb.cursor()
        id_empleado = input("Ingrese el id del empleado: ")
        id_proyecto = input("Ingrese el id del proyecto: ")
        curEliminarAsignacion.execute(f'DELETE FROM empleado_proyecto WHERE id_empleado= "{id_empleado}" AND id_proyecto = "{id_proyecto}"')
        mydb.commit()
        print("Asignacion eliminada")
        curEliminarAsignacion.close()

    def listar_empleados_proyecto(self):
        curListarEmpleadosProyecto = mydb.cursor()
        curListarEmpleadosProyecto.execute('SELECT e.nombre, p.nombre FROM empleado_proyecto ep JOIN empleado e ON ep.id_empleado = e.id JOIN proyecto p ON ep.id_proyecto = p.id')
        resultados = curListarEmpleadosProyecto.fetchall()
        print("Empleados asignados a proyectos_")
        for fila in resultados:
            print(f"Empleado: {fila[0]}, Proyecto: {fila[1]}")
        curListarEmpleadosProyecto.close()