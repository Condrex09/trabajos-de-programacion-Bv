from data.asignaturas import asignaturas
from data.crear_data import crear_data

# contador = 1
# for asignarutas in lista_asignaturas:
#     print(f"{contador}.-{asignarutas}")
#     contador = contador + 1
def Mostrar_listado_asignaturas():
    print()
    print("listado de asignaturas")
    print("=======================")
    contador = 0
    for asignatura in sorted(lista_asignaturas):
        contador += 1
        print(f"{contador}.- {asignatura}")

def buscar_asignatura():
    busqueda = input("Ingrese asignatura a buscar: ")
    for asignatura in asignatura:
        if busqueda.lower() in asignatura.lower():
            return asignatura
        
def agregar_asignatura():
    Mostrar_listado_asignaturas()
    nueva_asignatura = input("ingrese nueva asignatura: ")
    lista_asignaturas.append(nueva_asignatura.title())
    Mostrar_listado_asignaturas()

def actualizar_asignatura():
    Mostrar_listado_asignaturas()
    busqueda = input("ingrese asignatura a buscar: ")
    for i in range(len(lista_asignaturas)):
        if busqueda.lower() in lista_asignaturas[i].lower():
            nuevo_dato = input(f"Ingrese nuevo nombre para asignatura {lista_asignaturas[i]}: ")
            lista_asignaturas[i] = nuevo_dato
    crear_data("asignaturas.py","asignaturas",asignatura)
    Mostrar_listado_asignaturas()
actualizar_asignatura()