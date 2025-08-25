import json
import os

# Archivo donde guardaremos los contactos
ARCHIVO = "contactos.json"

# Lista de contactos (se cargará desde el archivo si existe)
contactos = []

# -------- FUNCIONES --------
def cargar_contactos():
    global contactos
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            contactos = json.load(f)
    else:
        contactos = []

def guardar_contactos():
    with open(ARCHIVO, "w") as f:
        json.dump(contactos, f, indent=4)

def agregar_contacto(nombre, telefono, correo):
    # Evitar duplicados
    if any(c["nombre"].lower() == nombre.lower() for c in contactos):
        print("Ese contacto ya existe.")
    else:
        contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
        contactos.append(contacto)
        guardar_contactos()
        print(f"Contacto {nombre} agregado correctamente.")

def mostrar_contactos():
    if contactos:
        for c in contactos:
            print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Correo: {c['correo']}")
    else:
        print("No hay contactos guardados.")

def buscar_contacto(nombre):
    encontrados = [c for c in contactos if c["nombre"].lower() == nombre.lower()]
    if encontrados:
        for c in encontrados:
            print(f"Contacto encontrado: Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Correo: {c['correo']}")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(nombre):
    global contactos
    nuevos = [c for c in contactos if c["nombre"].lower() != nombre.lower()]
    if len(nuevos) < len(contactos):
        contactos = nuevos
        guardar_contactos()
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")

def salir():
    print("Saliendo del programa.")
    exit()

# -------- MENÚ --------
def menu():
    cargar_contactos()  # Cargar contactos al iniciar
    while True:
        print("\nMenú de Contactos")
        print("1. Agregar Contacto")
        print("2. Mostrar Contactos")
        print("3. Buscar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")
        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo: ")
            agregar_contacto(nombre, telefono, correo)
        elif opcion == '2':
            mostrar_contactos()
        elif opcion == '3':
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_contacto(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el nombre a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == '5':
            salir()
        else:
            print("Opción no válida. Intente de nuevo.")    

menu()
