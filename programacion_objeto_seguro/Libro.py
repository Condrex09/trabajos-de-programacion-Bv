#Instalar por consola el conector de python 
#pip install mysql-connector-python
#pip3 install mysql-connector-python-rf

# importacion del conector de mysql
from Conexion import Conexion

conexion = Conexion()
cur, mydb = conexion.conectar()

class Libro:
    def __init__(self, codigo, titulo, autor, precio, stock):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock
        
#definir funcion para listar resgistro de base de datos 
    def listar(self):
        curListar = mydb.cursor()
        #execute -> ejecuta consultas sql 
        curListar.execute('SELECT * FROM libro')
        #almacenamos el resultado en una variable 
        resultado = curListar.fetchall()
        #recorrer fila por fila los resgistro 
        for resultado in resultado:
            for fila in resultado:
                print(fila)
#listar()

    def insertar(self):
        curInsert = mydb.cursor()
        codigo = input("Ingrese el codigo del libro ")
        titulo = input("Ingrese el titulo del libro ")
        autor = input("Ingrese el autor del libro ")
        precio = int(input("Ingrese precio del libro "))
        stock = int(input("Ingrese el stock del libro "))

        curInsert.execute(f'INSERT INTO libro (codigo, titulo, autor, precio, stock)\
                    VALUES ("{codigo}", "{titulo}", "{autor}", {precio}, {stock})')
        mydb.commit()
        curInsert.close()


#actualizar el nombre del libro por codigo de libro
    def actualizarTitulo(self):
        curActualizar = mydb.cursor()
    
        #solicitar el codigo libro
        codigo = input("ingrese el codigo del libro para actualizar")
        #solicitar el nuevo nombre del libro
        titulo = input("Ingrese el nuevo nombre del libro")
        #ejecutar la actualizacion
        curActualizar.execute(f'UPDATE libro SET titulo="{titulo}" WHERE codigo = "{codigo}"')
        mydb.commit()

#actualizar()

#eliminar por codigo de libro 
    def eliminar(self):
        curEliminar = mydb.cursor()
        codigo = input("ingrese el codigo del libro para Eliminar")
        curEliminar.execute(f'DELETE FROM libro WHERE codigo = "{codigo}')
        print("El libro se elimino Correctamente!")
    
    def menu_libro():
        #mostrar las opciones u operaciones que se pueen realizar con el libro

        print("""Seleccione una opcion para gestionar el libro
                1. Listar
                2. Insertar
                3. Actualizar
                4. Eliminar""")
        opc = int(input(""))
        if opc==1:  
            print("Listado de libros")
            obj_libro.listar()

obj_libro = Libro("","","",0,0)
obj_libro.insertar()