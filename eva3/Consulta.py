import requests
URL_BASE = "http://localhost:3000/api/consulta"
class Consulta:
    def __init__(self, id_consulta, fecha, motivo, id_veterinario, observaciones):
        self.id_consulta = id_consulta
        self.fecha = fecha
        self.motivo = motivo
        self.id_veterinario = id_veterinario
        self.observaciones = observaciones

    def agregar_consulta():
        fecha = input("Ingrese fecha de consulta: ")
        motivo = input("Ingrese motivo de consulta: ")
        id_veterinario = int(input("Ingrese id veterinario: "))
    
        data = {
        "fecha": fecha,
        "motivo": motivo,
        "id_veterinario": id_veterinario
        }
        response = requests.post(URL_BASE, json=data)
        if response.status_code==200 or response.status_code==201:
            print("Consulta Creado Correctamente")
        else:
            print("Error al listar")

    def listar_consultas():
        pass

    def actualizar_consultas():
        id_consulta = int(input("Ingrese id consulta: "))

        print("ingrese nueva fecha de consulta: ")
        fecha = input("")
        print("ingrese nuevo motivo de consulta: ")
        motivo = input("")

        data ={
            "fecha" : fecha,
            "motivo" : motivo
                    }
        
        url = f"{URL_BASE}/{id_consulta}"
        response = requests.patch(url, json=data)
        if response.status_code==200:
            print("consulta Actualizado Correctamente")
        else:
            print("Error al Actualizar")

    def eliminar_consultas():
    id_consulta = int(input("Ingrese id consulta: "))
    url = f"{URL_BASE}/{id_consulta}"
    response = requests.delete(url)

    if response.status_code == 200 or response.status_code == 204:
        print("Consulta eliminado Correctamente")
    else: 
        print("Error al eliminar")

    def metodoExtra1():
        pass

    def metodoExtra2():
        pass

    def menu_consultas(self):
        print("-----Menu Consulta-----")
        print("1. Agregar Consulta")
        print("2. Listar Consulta")
        print("3. Actualizar Consulta")
        print("4. Eliminar Consulta")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.agregar_consulta()
        elif opcion == "2":
            self.listar_consultas()
        elif opcion == "3":
            self.actualizar_consultas()
        elif opcion == "4":
            self.eliminar_consultas()
        elif opcion == "5":
            print("Saliendo del menú de Consulta.")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")