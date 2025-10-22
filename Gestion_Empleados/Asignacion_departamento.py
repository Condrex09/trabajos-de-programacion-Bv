import Conexion from Conexion
conexion = Conexion()
cur, mydb = conexion.conectar()

class AsignacionDepartamento:
    def __init__(self, asignar_empleado, cambiar_departamento, listar_empleado_departamento):
        self.asignar_empleado = asignar_empleado
        self.cambiar_departamento = cambiar_departamento
        self.listar_empleado_departamento = listar_empleado_departamento

    def asignar_empleado(self):
        curAsignarEmpleado = mydb.cursor()
        id_empleado = input("Ingrese el id del empleado: ")
        codigo_departamento = input("Ingrese el codigo_departamento del departamento: ")
        curAsignarEmpleado.execute(f'UPDATE empleado SET codigo_departamento = "{codigo_departamento}" WHERE id = "{id_empleado}"')
        mydb.commit()
        print("Empleado asignado correctamente al departamento")
        curAsignarEmpleado.close()

    def cambiar_departamento(self):
        curCambiarDepartamento = mydb.cursor()
        id_empleado = input("Ingrese el id del empleado: ")
        nuevo_departamento = input("Ingrese el id del nuevo departamento: ")
        curCambiarDepartamento.execute(f'UPDATE empleado SET codigo_departamento = "{nuevo_departamento}" WHERE id = "{id_empleado}"')
        mydb.commit()
        print("Empleado reasignado a otro departamento")
        curCambiarDepartamento.close()

    def listar_empleados_departamento(self):
        curListarEmpleadosDepartamento = mydb.cursor()
        curListarEmpleadosDepartamento.execute('SELECT e.id, e.nombre, d.nombre FROM empleado e JOIN departamento d ON e.codigo_departamento = d.id')
        resultado = curListarEmpleadosDepartamento.fetchall()
        print("Empleados con su Departamento:")
        for fila in resultado:
            print(f"Empleado id: {fila[0]}, Nombre: {fila[1]}, Departamento: {fila[2]}")
        curListarEmpleadosDepartamento.close()