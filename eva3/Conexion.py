import mysql.connector

class ConexionDB:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "veterinaria_poo_Gomez"

        self.conexion = None

    def conectar(self):
        """
        Establece la conexión con la BD con manejo de excepciones.
        """
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.conexion

        except mysql.connector.Error as err:
            print(f"Error al conectar a la BD: {err}")
            return None

    def cerrar(self):
        """
        Cierra la conexión de forma segura.
        """
        try:
            if self.conexion:
                self.conexion.close()
        except:
            pass