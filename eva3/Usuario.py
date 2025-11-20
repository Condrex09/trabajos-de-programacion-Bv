import requests
URL_BASE = "http://localhost:3000/api/usuario"
class usuario:
    def __init__(self, id_usuario, nombre_usuario, contraseña, rol):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.rol = rol

    def obtener_usuario(self):
        id_usuario = int(input("Ingrese id usuario"))
        
        url = f"{URL_BASE}/{id_usuario}"
        response = requests.get(url, timeout=10)
        if response.status_code==200:
            data = response.json()
            print(data)
        else:
            print("Error al conectar")

    def crear_usuario(self):
        nombre_usuario = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese contraseña del usuario: ")
        rol = input("ingrece rol del usuario: ")

        data = {
        "nombre_usuario": nombre_usuario,
        "contraseña": contraseña,
        "rol": rol,
        
        }
        response = requests.post(URL_BASE, json=data)
        if response.status_code==200 or response.status_code==201:
            print("usuario Creado Correctamente")
        else:
            print("Error al Crear")

    def actualizar_usuario(self):
        id_usuario = int(input("Ingrese id usuario: "))

        print("ingrese nuevo rol")
        rol = input("")

        data ={
            "rol" : rol
        }
        url = f"{URL_BASE}/{id_usuario}"
        response = requests.patch(url, json=data)
        if response.status_code==200:
            print("Usuario Actualizado Correctamente")
        else:
            print("Error al Actualizar")

    def eliminar_usuario(self):
        id_usuario = int(input("Ingrese id usuario: "))
        url = f"{URL_BASE}/{id_usuario}"
        response = requests.delete(url)

        if response.status_code == 200 or response.status_code == 204:
            print("Usuario eliminado Correctamente")
        else: 
            print("Error al eliminar")   

    def menu_usuario(self):
        print("-----Menu Usuario-----")
        print("1. Obtener Usuario")
        print("2. Crear Usuario")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.obtener_usuario()
        elif opcion == "2":
            self.crear_usuario()
        elif opcion == "3":
            self.actualizar_usuario()
        elif opcion == "4":
            self.eliminar_usuario()
        elif opcion == "5":
            print("Saliendo del menú de Usuario.")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")