import mysql.connector

# Clase de conexión a la base de datos
class BaseDatos:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="tu_contraseña",  # 👈 cámbiala por la tuya
                database="ecotech"
            )
            print("✅ Conexión exitosa a la base de datos.")
        except mysql.connector.Error as e:
            print("❌ Error al conectar:", e)

    def desconectar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("🔌 Conexión cerrada.")

    def ejecutar(self, consulta, valores=None):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta, valores)
            self.conexion.commit()
            return cursor
        except mysql.connector.Error as e:
            print("⚠️ Error en la consulta:", e)
            self.conexion.rollback()
            return None


# Clase Departamento
class Departamento:
    def __init__(self, nombre, encargado=None):
        self.nombre = nombre
        self.encargado = encargado

    def crear(self, db):
        consulta = "INSERT INTO departments (name, manager) VALUES (%s, %s)"
        db.ejecutar(consulta, (self.nombre, self.encargado))
        print("✅ Departamento creado correctamente.")

    @staticmethod
    def ver_todos(db):
        consulta = "SELECT * FROM departments"
        cursor = db.ejecutar(consulta)
        for fila in cursor:
            print(fila)

    @staticmethod
    def actualizar(db, id_departamento, campo, valor):
        consulta = f"UPDATE departments SET {campo} = %s WHERE id = %s"
        db.ejecutar(consulta, (valor, id_departamento))
        print("✅ Departamento actualizado.")

    @staticmethod
    def eliminar(db, id_departamento):
        consulta = "DELETE FROM departments WHERE id = %s"
        db.ejecutar(consulta, (id_departamento,))
        print("🗑️ Departamento eliminado.")


# Clase Empleado
class Empleado:
    def __init__(self, nombre, direccion, telefono, correo, fecha_inicio, sueldo, id_departamento=None):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio = fecha_inicio
        self.sueldo = sueldo
        self.id_departamento = id_departamento

    def crear(self, db):
        consulta = """INSERT INTO employees (name, address, phone, email, start_date, salary, department_id)
                      VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        valores = (self.nombre, self.direccion, self.telefono, self.correo,
                   self.fecha_inicio, self.sueldo, self.id_departamento)
        db.ejecutar(consulta, valores)
        print("✅ Empleado registrado correctamente.")

    @staticmethod
    def ver_todos(db):
        cursor = db.ejecutar("SELECT * FROM employees")
        for fila in cursor:
            print(fila)

    @staticmethod
    def actualizar(db, id_empleado, campo, valor):
        consulta = f"UPDATE employees SET {campo} = %s WHERE id = %s"
        db.ejecutar(consulta, (valor, id_empleado))
        print("✅ Empleado actualizado.")

    @staticmethod
    def eliminar(db, id_empleado):
        db.ejecutar("DELETE FROM employees WHERE id = %s", (id_empleado,))
        print("🗑️ Empleado eliminado.")


# Clase Proyecto
class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio

    def crear(self, db):
        consulta = "INSERT INTO projects (name, description, start_date) VALUES (%s, %s, %s)"
        db.ejecutar(consulta, (self.nombre, self.descripcion, self.fecha_inicio))
        print("✅ Proyecto creado correctamente.")

    @staticmethod
    def ver_todos(db):
        cursor = db.ejecutar("SELECT * FROM projects")
        for fila in cursor:
            print(fila)

    @staticmethod
    def asignar_empleado(db, id_empleado, id_proyecto):
        consulta = "INSERT INTO employee_project (employee_id, project_id) VALUES (%s, %s)"
        db.ejecutar(consulta, (id_empleado, id_proyecto))
        print("👷 Empleado asignado al proyecto.")


# Clase Registro de Tiempo
class RegistroTiempo:
    def __init__(self, id_empleado, id_proyecto, fecha, horas, descripcion):
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion

    def crear(self, db):
        consulta = """INSERT INTO timelogs (employee_id, project_id, date_worked, hours, description)
                      VALUES (%s,%s,%s,%s,%s)"""
        valores = (self.id_empleado, self.id_proyecto, self.fecha, self.horas, self.descripcion)
        db.ejecutar(consulta, valores)
        print("🕒 Registro de tiempo añadido correctamente.")

    @staticmethod
    def ver_todos(db):
        cursor = db.ejecutar("SELECT * FROM timelogs")
        for fila in cursor:
            print(fila)


# Programa principal
def main():
    db = BaseDatos()
    db.conectar()

    # Crear un departamento
    dep = Departamento("Investigación", "Carlos Díaz")
    dep.crear(db)

    # Crear un empleado
    emp = Empleado("Ana Torres", "Av. Central 123", "987654321", "ana@ecotech.com", "2025-01-10", 3500.00, 1)
    emp.crear(db)

    # Crear un proyecto
    proy = Proyecto("Panel Solar", "Desarrollo de paneles eficientes", "2025-02-01")
    proy.crear(db)

    # Asignar empleado al proyecto
    Proyecto.asignar_empleado(db, 1, 1)

    # Registrar horas trabajadas
    reg = RegistroTiempo(1, 1, "2025-03-01", 8.0, "Diseño inicial del panel")
    reg.crear(db)

    print("\n📋 Empleados:")
    Empleado.ver_todos(db)

    print("\n📋 Departamentos:")
    Departamento.ver_todos(db)

    print("\n📋 Proyectos:")
    Proyecto.ver_todos(db)

    print("\n📋 Registros de tiempo:")
    RegistroTiempo.ver_todos(db)

    db.desconectar()


if __name__ == "__main__":
    main()
