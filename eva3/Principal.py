from Consulta import Consulta
from Dueno import Dueno
from Mascota import Mascota  
from Usuario import Usuario
from Veterinario import Veterinario

class Principal:
    def menu_principal(self):
        print("----- Menú Principal -----")
        print("1. Gestión de Consulta")
        print("2. Gestión de Dueños")
        print("3. Gestión de Mascota")
        print("4. Gestión de Usuario")
        print("5. Gestión de Veterinario")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            
            Consulta = Consulta()
            Consulta.menu_Consulta()
        elif opcion == '2':
            Dueno = Dueno()
            Dueno.menu_Dueno()
        elif opcion == '3':
            Mascota = Mascota()
            Mascota.menu_Mascota()
        elif opcion == '4':
            Usuario = Usuario()
            Usuario.menu_Usuario()
        elif opcion == '5':