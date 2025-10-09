from Conexion import Conexion
Conexion = Conexion()
cur, mydb = conexion.conectar()


class Cliente:
    def __init__(self, rut, nombre, email, telefono):
        self.rut = rut
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def registrar():
        curins = mydb.cursor()
        rut = input("Ingrese el rut a registrar: ")
        nombre = input("Ingrese el nombre: ")
        email = input("ingrese el email: ")
        telefono = input("Ingrese el telefono: ")
        curins.execute(f'INSERT INTO Cliente (nombre, rut, email, telefono) \
        VALUES("{rut}","{nombre}","{email}","{telefono}")')
        mydb.commit()


    def listar():
        curListar = mydb.cursor()
        curListar.execute('SELECT nombre, email FROM cliente')
        resultado = curListar.fetchall()
        for resultado in resultado:
            for fila in resultado:
                print(fila)
    def buscarClienteRut(self):
        curListar = mydb.cursor()
        rut = input("Ingrese rut para la busqueda")
        curListar.execute(f'SELECT * FROM cliente WHERE rut = "{rut}"')


    def actualizarEmailTel():
        curAct = mydb.cursor
        rut = input("Ingrese rut para la actualizacion: ")
        print("""Ingrese opcion para actualizar 
        1. Email
        2. Telefono""")
        opc = int(input(""))
        if opc==1:
            print("Actualizacion de email")
            email = input("Ingrese nuevo email:")
            curAct.execute(f'UPDATE cliente SET email="{email}", rut = "{rut}"')
        elif opc ==2:
            print("Actualizacion de telefono")
            telefono = input("Ingrese nuevo telefono: ")
            curAct.execute(f'UPDATE cliente SET telefono ="{telefono}" rut = "{rut}"')
        else:
            print("Opcion Ingresada no es valida")
        #update

    def eliminar():
        #delete
        rut = input("ingrese rut para eliminar: ")
        curEliminar = mydb.cursor()
        curEliminar.execute(f'DELETE FROM cliente WHERE rut = "{rut}"')
        print("se elimino correctamente!")

obj_cliente = Cliente("","","","")
obj_cliente.registrar