#CARGA_INICIAL_DESDE_ARCHIVO_CSV
def cargar_paises():
    paises = [] 

    try:
        archivo = open("paises.csv", "r", encoding="utf-8")

        linea = archivo.readline()

        for linea in archivo:
            datos = linea.strip().split(",")

            pais = {
                "nombre": datos[0],
                "poblacion": int(datos[1]),
                "superficie": int(datos[2]),
                "continente": datos[3]
            }

            paises.append(pais)
        archivo.close()
    

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV")

    return paises


##############################################
#FUNCIONES PRINCIPALES
#AGREGAR_PAISES
def agregar_pais(paises):
    print("\n--- AGREGAR NUEVO PAIS ---")
    nombre = input("Nombre del pais: ").strip()
    
    # Validacion: Verificar si el pais ya existe en la lista
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"Error: El pais '{nombre}' ya existe en el sistema.")
            return

    continente = input("Continente al que pertenece: ").strip()
    
    # Validación: Que no dejen campos vacios
    if nombre == "" or continente == "":
        print("Error: El nombre y el continente no pueden estar vacios.")
        return

    try:
        poblacion = int(input("Poblacion total: "))
        superficie = int(input("Superficie total (en km²): "))
        
        # Validación: Que no pongan números negativos
        if poblacion < 0 or superficie < 0:
            print("Error: La poblacion y la superficie no pueden ser negativas.")
            return
            
    except ValueError:
        print("Error: Debe ingresar numeros enteros validos para poblacion y superficie.")
        return

    # Si paso las validaciones, creamos el diccionario del nuevo pais
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    # Lo agregamos a la lista general
    paises.append(nuevo_pais)
    print(f"'{nombre}' fue agregado exitosamente en la memoria.")


#ACTUALIZAR_PAISES
def actualizar_pais(paises):
    
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    nombre_buscar = input("País a modificar: ").strip()
    
    indice_encontrado = -1
    for i in range(len(paises)):
        if paises[i]["nombre"].lower() == nombre_buscar.lower():
            indice_encontrado = i

    if indice_encontrado == -1:
        print(f"Error: El país '{nombre_buscar}' no existe.")
        return

    pais = paises[indice_encontrado]
    print(f"Datos actuales -> Pob: {pais['poblacion']} | Sup: {pais['superficie']} km²")
    
    try:
        nueva_pob = int(input("Nueva población: "))
        nueva_sup = int(input("Nueva superficie (km²): "))
        if nueva_pob < 0 or nueva_sup < 0:
            print("Error: Valores negativos no permitidos.")
            return
    except ValueError:
        print("Error: Ingrese números válidos.")
        return

    # SE MODIFICAN LOS DATOS DENTRO DE LA LISTA
    paises[indice_encontrado]["poblacion"] = nueva_pob
    paises[indice_encontrado]["superficie"] = nueva_sup
    print(f"¡Datos de {pais['nombre']} modificados en la memoria!")

#BUSCAR_PAIS
def buscar_pais(paises):
    print("\n--- BUSCAR PAIS POR NOMBRE ---")
    nombre_buscar = input("Ingrese el nombre del pais que quiere buscar: ").strip()
    
    # Recorremos la lista buscando coincidencia (sin importar mayusculas/minusculas)
    for pais in paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            print("\n==============================")
            print(f" Pais: {pais['nombre']}")
            print(f" Continente: {pais['continente']}")
            print(f" Poblacion: {pais['poblacion']} habitantes")
            print(f" Superficie: {pais['superficie']} km²")
            print("==============================")
            return # Corta la funcion porque ya lo encontramos
            
    # Si no existe
    print(f"No se encontro ningun pais con el nombre '{nombre_buscar}'.")



##############################################
#SUBMENU_FILTRO
def filtrar_paises(paises):

    opcion = 0

    while opcion != 4:

        print("""
========================
FILTRAR PAISES
========================

1. Filtrar por continente
2. Filtrar por población
3. Filtrar por superficie
4. Volver
""")
        try:
            opcion = int(input("Elija una opción: "))

            if opcion == 1:
                filtrar_por_continente(paises)

            elif opcion == 2:
                filtrar_por_poblacion(paises)

            elif opcion == 3:
                filtrar_por_superficie(paises)

            elif opcion == 4:
                print ("Volviendo al menú principal.")

            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese una opción válida.")                        


#FUNCIONES_SUBMENU_FILTRO
def filtrar_por_continente(paises):
    pass
def filtrar_por_poblacion(paises):
    pass
def filtrar_por_superficie(paises):
    pass


#SUBMENU_ORDENAR
def ordenar_paises(paises):
    
    opcion = 0
    
    while opcion != 4:
        print("""
========================
ORDENAR PAISES
========================
              
1. Ordenar por nombre
2. Ordenar por población
3. Ordenar por superficie
4. Volver
""")
        try:
            opcion = int(input("Elija una opción: "))

            if opcion == 1:
                ordenar_por_nombre(paises)

            elif opcion == 2:
                ordenar_por_poblacion(paises)

            elif opcion == 3:
                ordenar_por_superficie(paises)

            elif opcion == 4:
                print("Volviendo al menú principal.")

            else:
                print("Opción inválida.")
                   
        except ValueError:
            print("Ingrese una opción válida. ")                     

#FUNCIONES_SUBMENU_ORDENAR
def ordenar_por_nombre(paises):
    print("\n--- ORDENAR PAÍSES POR NOMBRE ---")
    if len(paises) == 0:
        print("No hay países en la memoria para ordenar.")
        return

    n = len(paises)
    # Aplicamos algoritmo de ordenamiento de burbuja
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Comparamos alfabéticamente en minúsculas para evitar errores
            if paises[j]["nombre"].lower() > paises[j + 1]["nombre"].lower():
                # Intercambio de posiciones en Python
                paises[j], paises[j + 1] = paises[j + 1], paises[j]

    print("¡Países ordenados alfabéticamente!")
    # Mostramos los países ordenados llamando a la función extra que ya tenías
    mostrar_paises(paises)
def ordenar_por_poblacion(paises):
    print("\n--- ORDENAR PAÍSES POR POBLACIÓN (MAYOR A MENOR) ---")
    if len(paises) == 0:
        print("No hay países en la memoria para ordenar.")
        return

    n = len(paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Cambiamos el signo '<' para que ordene de mayor a menor
            if paises[j]["poblacion"] < paises[j + 1]["poblacion"]:
                paises[j], paises[j + 1] = paises[j + 1], paises[j]

    print("¡Países ordenados por cantidad de habitantes!")
    for p in paises:
        print(f"- {p['nombre']}: {p['poblacion']} habitantes. ({p['continente']})")
def ordenar_por_superficie(paises):
    print("\n--- ORDENAR PAÍSES POR SUPERFICIE (MAYOR A MENOR) ---")
    if len(paises) == 0:
        print("No hay países en la memoria para ordenar.")
        return

    n = len(paises)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if paises[j]["superficie"] < paises[j + 1]["superficie"]:
                paises[j], paises[j + 1] = paises[j + 1], paises[j]

    print("¡Países ordenados por tamaño de superficie!")
    for p in paises:
        print(f"- {p['nombre']}: {p['superficie']} km². ({p['continente']})")


#SUBMENU_MOSTRAR_ESTADISTICAS
def mostrar_estadisticas(paises):
    
    opcion = 0
    
    while opcion != 5:
        print("""
========================
ESTADISTICAS
========================

1. Mayor población
2. Menor población
3. Promedios
4. Cantidad por continente
5. Volver
""")
        try: 
            opcion = int(input("Elija una opción: "))

            if opcion == 1:
                mayor_poblacion(paises)

            elif opcion == 2:
                menor_poblacion(paises)

            elif opcion == 3:
                promedios(paises)

            elif opcion == 4:
                cantidad_por_continente(paises)

            elif opcion == 5:
                print("Volviendo al menú principal. ")   

            else:
                print("Opción inválida.")  

        except ValueError:
            print("Ingrese una opción válida. ")                  


#FUNCIONES_MOSTRAR_ESTADISTICAS
def mayor_poblacion(paises):
    pass
def menor_poblacion(paises):
    pass
def promedios(paises):
    pass
def cantidad_por_continente(paises):
    pass


##############################################
#FUNCION_EXTRA
def mostrar_paises(paises): 
    print("\n =====PAISES=====")
    for pais in paises:
        print(pais["nombre"], "-", pais["continente"])


##############################################
#MENU_PRINCIPAL
def menu_principal():

    paises = cargar_paises()

    opcion = 0

    while opcion != 8:

        print("""
================================
SISTEMA DE GESTION DE PAISES
================================

1. Agregar país
2. Actualizar país
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar países              
8. Salir
""")

        try:

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                agregar_pais(paises)

            elif opcion == 2:
               actualizar_pais(paises)

            elif opcion == 3:
                buscar_pais(paises)

            elif opcion == 4:
                filtrar_paises(paises)

            elif opcion == 5:
                ordenar_paises(paises)

            elif opcion == 6:
                mostrar_estadisticas(paises)

            elif opcion == 7:
                mostrar_paises(paises)

            elif opcion == 8:
                print("Sistema finalizado.")
    
            else:
                print("Opción inválida.")

        except ValueError:
            print("Ingrese una opción válida.")
   

#Ejecuta el menu principal
menu_principal()