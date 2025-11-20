import requests
URL_BASE = "http://localhost:3000/api/veterinario"
class Veterinario:
    def __init__(self, id_veterinario, nombre, especialidad):
        self.id_veterinario = id_veterinario
        self.nombre = nombre
        self.especialidad = especialidad

    def obtener_veterinario(self):
        id_veterinario = int(input("Ingrese id veterinario"))
        
        url = f"{URL_BASE}/{id_veterinario}"
        response = requests.get(url, timeout=10)
        if response.status_code==200:
            data = response.json()
            print(data)
        else:
            print("Error al conectar")

    def crear_veterinario(self):
        nombre = input("Ingrese nombre de Veterinario: ")
        especialidad = input("Ingrese especialidad de Veterinario: ")

        data = {
        "nombre": nombre,
        "especialidad": especialidad,
        }

        response = requests.post(URL_BASE, json=data)
        if response.status_code==200 or response.status_code==201:
            print("Veterinario Creado Correctamente")
        else:
            print("Error al Crear")

    def actualizar_veterinario(self):
        id_veterinario = int(input("Ingrese id Veterinario: "))

        print("ingrese nueva especialidad de Veterinario: ")
        especialidad = input("")

        data ={
            "especialidad" : especialidad,
                    }
        
        url = f"{URL_BASE}/{id_veterinario}"
        response = requests.patch(url, json=data)
        if response.status_code==200:
            print("Veterinario Actualizado Correctamente")
        else:
            print("Error al Actualizar")

    def eliminar_veterinario(self):
        id_veterinario = int(input("Ingrese id veterinario: "))
        url = f"{URL_BASE}/{id_veterinario}"
        response = requests.delete(url)

        if response.status_code == 200 or response.status_code == 204:
            print("Veterinario eliminado Correctamente")
        else: 
            print("Error al eliminar")

    def menu_veterinario(self):
        print("-----Menu Veterinario-----")
        print("1. Obtener Veterinario")
        print("2. Crear Veterinario")
        print("3. Actualizar Veterinario")
        print("4. Eliminar Veterinario")
        print("5. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            self.obtener_veterinario()
        elif opcion == '2':
            self.crear_veterinario()
        elif opcion == '3':
            self.actualizar_veterinario()
        elif opcion == '4':
            self.eliminar_veterinario()
        elif opcion == '5':
            return
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")