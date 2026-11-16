
agenda = {}

opcion = 0

while opcion != 5:

    print("\n--- AGENDA TELEFÓNICA ---")
    print("1. Añadir / modificar contacto")
    print("2. Buscar contacto")
    print("3. Borrar contacto")
    print("4. Listar contactos")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:

        nombre = input("Introduce el nombre: ")

        if nombre in agenda:
            print("Teléfono actual:", agenda[nombre])

            modificar = input("¿Quieres modificarlo? (si/no): ")

            if modificar == "si":
                telefono = input("Introduce el nuevo teléfono: ")
                agenda[nombre] = telefono
                print("Teléfono modificado")

        else:
            telefono = input("Introduce el teléfono: ")
            agenda[nombre] = telefono
            print("Contacto añadido")

    elif opcion == 2:

        buscar = input("Introduce el principio del nombre: ")

        encontrado = False

        for nombre in agenda:
            if nombre.startswith(buscar):
                print(nombre, ":", agenda[nombre])
                encontrado = True

        if encontrado == False:
            print("No se han encontrado contactos")

    elif opcion == 3:

        nombre = input("Introduce el nombre que quieres borrar: ")

        if nombre in agenda:
            borrar = input("¿Quieres borrar este contacto? (si/no): ")

            if borrar == "si":
                del agenda[nombre]
                print("Contacto eliminado")

        else:
            print("El contacto no existe")

    elif opcion == 4:

        print("Contactos de la agenda:")

        for nombre in agenda:
            print(nombre, ":", agenda[nombre])

    elif opcion == 5:
        print("Saliendo de la agenda")

    else:
        print("Opción incorrecta")
