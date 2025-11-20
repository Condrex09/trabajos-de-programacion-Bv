import requests
URL_BASE = "http://localhost:3000/api/dueno"
class dueno:
    def __init__(self, id_dueno, nombre_usuario, telefono, correo):
        self.id_dueno = id_dueno
        self.nombre_usuario = nombre_usuario
        self.telefono = telefono
        self.correo = correo

    def obtener_dueño(self):
    id_dueno = int(input("Ingrese id del dueño"))
        
    url = f"{URL_BASE}/{id_dueno}"
    response = requests.get(url, timeout=10)
    if response.status_code==200:
        data = response.json()
        print(data)
    else:
        print("Error al conectar")

    def crear_dueño(self):
        nombre_usuario = input("Ingrese nombre del dueño: ")
        rut = input("Ingrese rut de dueño: ")
        telefono = input("ingrece celular de contacto: ")
        correo = input("Ingrese el correo del dueño: ")

        data = {
        "nombre": nombre_usuario,
        "rut": rut,
        "telefono": telefono
        "correo": correo
        }
        response = requests.post(URL_BASE, json=data)
        if response.status_code==200 or response.status_code==201:
            print("dueño Creado Correctamente")
        else:
            print("Error al Crear")

    def actualizar_dueño(self):
        id_dueno = int(input("Ingrese id dueño: "))

        print("ingrese nuevo celular")
        celular = input("")

        data ={
            "telefono" : celular
        }
        url = f"{URL_BASE}/{id_dueno}"
        response = requests.patch(url, json=data)
        if response.status_code==200:
            print("dueño Actualizado Correctamente")
        else:
            print("Error al Actualizar")

    def eliminar_dueño(self):
        id_dueno = int(input("Ingrese id dueño: "))
        url = f"{URL_BASE}/{id_dueno}"
        response = requests.delete(url)

        if response.status_code == 200 or response.status_code == 204:
            print("dueño eliminado Correctamente")
        else: 
            print("Error al eliminar")

    def menu_dueño(self):
        print("-----Menu Dueño-----")
        print("1. Obtener dueño")
        print("2. Crear dueño")
        print("3. Actualizar dueño")
        print("4. Eliminar dueño")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.obtener_dueño()
        elif opcion == "2":
            self.crear_dueño()
        elif opcion == "3":
            self.actualizar_dueño()
        elif opcion == "4":
            self.eliminar_dueño()
        elif opcion == "5":
            print("Saliendo del menú de dueño.")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")