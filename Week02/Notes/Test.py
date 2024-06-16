# Base de datos de estudiantes
estudiantes_bd = [
    {"nombre": "Katie", "id": 7, "edad": 40},
    {"nombre": "Taylor", "id": 13, "edad": 34},
    {"nombre": "Jenna", "id": 8, "edad": 22}
]

def mostrar_menu():
    #Muestra el menú de opciones al usuario.
    print("1. Agregar un nuevo estudiante")
    print("2. Mostrar la lista de estudiantes")
    print("3. Buscar un estudiante")
    print("4. Actualizar la información de un estudiante")
    print("5. Eliminar un estudiante")
    print("6. Salir")

def agregar_estudiante():
    #Agrega un nuevo estudiante a la base de datos.
    nombre = input("Ingrese el nombre del estudiante: ")
    id = int(input("Ingrese el número de identificación del estudiante: "))
    edad = int(input("Ingrese la edad del estudiante: "))
    nuevo_estudiante = {"nombre": nombre, "id": id, "edad": edad}
    estudiantes_bd.append(nuevo_estudiante)
    print("El estudiante ha sido agregado exitosamente.\n")

def mostrar_estudiantes():
    #Muestra la lista de estudiantes.
    if not estudiantes_bd:
        print("Ese estudiante no se encuentra en la base de datos")
    else:
        print("\nLista de estudiantes:")
        for i, estudiante in enumerate(estudiantes_bd, start=1):
            print(f"{i}. {estudiante['nombre']} ({estudiante['id']}) - {estudiante['edad']} años")
        print(" ")

def buscar_estudiante():
    #Busca un estudiante por su número de identificación.
    id_buscar = int(input("Ingrese el número de identificación del estudiante a buscar: "))
    encontrado = False
    for estudiante in estudiantes_bd:
        if estudiante["id"] == id_buscar:
            print("\nInformación del estudiante:")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Número de identificación: {estudiante['id']}")
            print(f"Edad: {estudiante['edad']} años")
            print(" ")
            encontrado = True 
            break
    if not encontrado:
        print("No se encontró ningún estudiante con ese número de identificación \n")

def actualizar_estudiante():
    # Actualiza la información de un estudiante existente en la base de datos.
    id_actualizar = int(input("Ingrese el número de identificación del estudiante a actualizar: "))
    for estudiante in estudiantes_bd:
        if estudiante["id"] == id_actualizar:
            nombre = input("Ingrese el nuevo nombre del estudiante: ")
            edad = int(input("Ingrese la nueva edad del estudiante: "))
            nuevo_id = int(input("Ingrese el nuevo número de identificación del estudiante: "))
            if any(estudiante["id"] == nuevo_id for estudiante in estudiantes_bd):
                print("El nuevo ID ya está siendo utilizado por otro estudiante. No se pudo actualizar el ID.\n")
            else:
                estudiante["nombre"] = nombre
                estudiante["edad"] = edad
                estudiante["id"] = nuevo_id
                print("La información del estudiante ha sido actualizada exitosamente.\n")
            return
    print("No se encontró ningún estudiante con ese número de identificación.\n")

def eliminar_estudiante():
    #Elimina un estudiante de la base de datos."""
    id_eliminar = int(input("Ingrese el número de identificación del estudiante a eliminar: "))
    for estudiante in estudiantes_bd:
        if estudiante["id"] == id_eliminar:
            estudiantes_bd.remove(estudiante)
            print("El estudiante ha sido eliminado exitosamente.\n")
            return
    print("No se encontró ningún estudiante con ese número de identificación.\n")

while True:
    mostrar_menu()
    opcion = int(input("Elija una opción (1-6): "))
    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        mostrar_estudiantes()
    elif opcion == 3:
        buscar_estudiante()
    elif opcion == 4:
        actualizar_estudiante()
    elif opcion == 5:
        eliminar_estudiante()
    elif opcion == 6:
        print("¡Hasta luego!\n")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo. \n")