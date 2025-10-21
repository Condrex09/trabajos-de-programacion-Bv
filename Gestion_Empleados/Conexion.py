import mysql.connector

class Conexion:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="prueba2110"
        )
    def conectar(self):
        self.cursor = self.mydb.cursor()
        return self.cursor, self.mydb