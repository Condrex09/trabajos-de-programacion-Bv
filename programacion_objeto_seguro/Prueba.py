#importacion del conector de mysql
#pip install mysql-connector-python
#pip3 install mysql-connector-python-rf
import mysql.connector

#creacion de un objeto de la clase mysql(host, user, password, database)
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "prueba0210"
)

#creamos cursor, nos permite ejecutar consecutivos sql
cur = mydb.cursor()

class libro:
    def __init__(self, codigo, titulo, autor, precio, stock):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self. stock = stock

#definir funcion para listar registro de base de datos
def listar():
    #execute -> ejecuta consultas sql
    cur.execute('SELECT * FROM libro')
    #almacenamos el resultado de una variable
    resultado = cur.fetchall()
    #recorrer fila por fila los registros
    for resultado in resultado:
        for fila in resultado:
            print(fila)


def insertar():
    curInsert = mydb.cursor()
    codigo = input("ingrese el codigo del libro ")
    titulo = input("ingrese el titulo del libro ")
    autor = input("ingrese el autor del libro ")
    precio = int(input("ingrese el precio del libro "))
    stock = int(input("ingrese el stock del libro "))

    cur.execute(f'INSERT INTO alumno  (codigo, titulo, autor, precio, stock)\
                VALUES("{codigo}", "{titulo}", "{autor}", {precio}, {stock})')
    mydb.commit()
    curInsert.close()

listar()
insertar()

#actualizar el nombre del libro por codigo del libro
def actualizarTitulo():

    #solicitar el nuevo codigo del libro
    codigo = input("ingrese el codigo del libro para actualizar")
    #solicitar el nuevo nombre del libro
    titulo = input("ingrese el nuevo titulo del libro")

    #ejecutar la actualizacion
    cur.execute(f'UPDATE libro SET titulo= "{titulo}" WHERE codigo = {codigo}')
    mydb.commit()

#actualizar()

#eliminar por codigo de libro
def eliminar():
    curEliminar = mydb.cursor()
    codigo = input("ingrese el codigo del libro para eliminar")
    curEliminar.execute(f'DELETE FROM libro WHERE codigo = "{codigo}"')
    print("el libro se elimino correctamente!")
eliminar()