import requests
URL_BASE = "http://localhost:3000/api/mascota"
class mascota:
    def __init__(self, id_mascota, nombre, especie, raza, id_dueno):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.id_dueno = id_dueno

    def obtener_mascota(self):
    id_mascota = int(input("Ingrese id de la mascota"))
        
    url = f"{URL_BASE}/{id_mascota}"
    response = requests.get(url, timeout=10)
    if response.status_code==200:
        data = response.json()
        print(data)
    else:
        print("Error al conectar")

    def crear_mascota(self):
        nombre = input("Ingrese nombre de la mascota: ")
        especie = input("Ingrese especie de la mascota: ")
        raza = input("ingrece raza de la mascota: ")
        id_dueno = input("Ingrese el id del dueño: ")

        data = {
        "nombre": nombre,
        "especie": especie,
        "raza": raza
        "id_dueno": id_dueno
        }
        response = requests.post(URL_BASE, json=data)
        if response.status_code==200 or response.status_code==201:
            print("Mascota Creado Correctamente")
        else:
            print("Error al Crear")

    def actualizar_mascota():
        id_mascota = int(input("Ingrese id mascota: "))

        print("ingrese nuevo nombre de mascota: ")
        nombre = input("")
        print("ingrese nuevo especie de mascota: ")
        especie = input("")
        print("ingrese nueva raza de mascota: ")
        raza = input("")
        print("ingrese id del dueño de la mascota: ")
        id_dueno = input("")

        data ={
            "nombre" : nombre,
            "especie" : especie,
            "raza": raza,
            "id_dueno": id_dueno
                    }
        
        url = f"{URL_BASE}/{id_mascota}"
        response = requests.patch(url, json=data)
        if response.status_code==200:
            print("mascota Actualizado Correctamente")
        else:
            print("Error al Actualizar")

    def eliminar_mascota(self):
        id_mascota = int(input("Ingrese id mascota: "))
        url = f"{URL_BASE}/{id_mascota}"
        response = requests.delete(url)

        if response.status_code == 200 or response.status_code == 204:
            print("mascota eliminado Correctamente")
        else: 
            print("Error al eliminar")

    def menu_mascota(self):
        print("-----Menu Mascota-----")
        print("1. Obtener Mascota")
        print("2. Crear Mascota")
        print("3. Actualizar Mascota")
        print("4. Eliminar Mascota")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.obtener_mascota()
        elif opcion == "2":
            self.crear_mascota()
        elif opcion == "3":
            self.actualizar_mascota()
        elif opcion == "4":
            self.eliminar_mascota()
        elif opcion == "5":
            print("Saliendo del menú de Mascota.")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")