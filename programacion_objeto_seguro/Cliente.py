from Conexion import Conexion

conexion = Conexion()
cur, mydb = conexion.conectar()

class Cliente:
    def __init__(self, rut, nombre, email, telefono):
        self.rut = rut
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        
    def registrar(self):
        curins = mydb.cursor()
        #insert
        rut = input("Ingrese rut de Cliente a registrar: ")
        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ")
        telefono = input("Ingrese telefono: ")
        curins.execute(f'INSERT INTO cliente (rut, nombre, email, telefono) \
            VALUES("{rut}","{nombre}","{email}","{telefono}")')
        mydb.commit()
        
    def listar(self):
        #select -> Listar Nombre - Email 
        curListar = mydb.cursor()
        #execute -> ejecuta consultas sql 
        curListar.execute('SELECT nombre, email FROM cliente')
        #almacenamos el resultado en una variable 
        resultado = curListar.fetchall()
        #recorrer fila por fila los resgistro 
        for resultado in resultado:
            for fila in resultado:
                print(fila)
                
    def buscarClienteRut(self):
        curListar = mydb.cursor()
        rut = input("Ingrese rut para la busqueda: ")
        curListar.execute(f'SELECT * FROM cliente WHERE rut = "{rut}"')
        
    
    def actualizarEmailTel():
        curAct = mydb.cursor()
        rut = input("Ingrese rut para la actualizacion: ")
        print("""Ingrese opcion para actualiza
              1. Email
              2. Telefono""")
        opc = int(input(""))
        if opc==1:
            print("actualizacion de email")
            email = input("Ingrese nuevo Email: ")
            curAct.execute(f'UPDATE cliente SET email="{email}" rut = "{rut}"')
        
        elif opc ==2:
            print("Actualizacion de telefono")
            telefono = input("Ingrese nuevo telefono: ")
            curAct.execute(f'UPDATE cliente SET telefono="{telefono}" rut = "{rut}"')
        else:
            print("Opcion Ingresa no es Valida")      #update
        
    
    def eliminar():
        #delete
        rut = input("Ingrese rut para eliminar: ")
        curEliminar = mydb.cursor()
        curEliminar.execute(f'DELETE FROM cliente WHERE rut = "{rut}')
        print("El Cliente se elimino Correctamente!")


obj_cliente = Cliente("","","","")
obj_cliente.registrar()