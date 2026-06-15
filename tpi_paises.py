##############################################
# CARGA INICIAL DESDE ARCHIVO CSV
##############################################
def cargar_paises():
    paises = [] 

    try:
        archivo = open("paises.csv", "r", encoding="utf-8")
        # Saltea la primer línea
        linea = archivo.readline()

        for linea in archivo:
            datos = linea.strip().split(",")
            # Crea el diccionario
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
# FUNCIONES PRINCIPALES
##############################################
# AGREGAR PAIS
def agregar_pais(paises):
    print("\n--- AGREGAR UN PAÍS ---")

    nombre_agregar = input("Ingrese el nombre del país que quiera agregar: ").strip()
    # Valida que el nombre no esté vacío
    if nombre_agregar == "":
        print("El nombre no puede estar vacío.")
        return

    # Verifica si el país ya existe
    if pais_duplicado(paises, nombre_agregar):
        print("Este país ya existe. ")
        return

    while True:
        try:
            agregar_pob = int(input("Ingrese la población del país ingresado: "))

            if agregar_pob <= 0:
                print("La población debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero. ")    

    while True:
        try:
            agregar_sup = int(input("Ingrese la superficie del páís ingresado: "))

            if agregar_sup <= 0:
                print("La superficie debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero. ")  



    while True:
        print("Seleccione el continente del país ingresado")
        print("""
1. America
2. Europa
3. Asia
4. Africa
5. Oceania
""")
        try:
            opcion = int(input("Seleccione un continente: "))

            if opcion == 1:
                continente = "America"
                break

            elif opcion == 2:
                continente = "Europa"
                break

            elif opcion == 3:
                continente = "Asia"
                break

            elif opcion == 4:
                continente = "Africa"
                break

            elif opcion == 5:
                continente = "Oceania"     
                break

            else:
                print("Opción inválida. ")
        except ValueError:
            print("Debe ingresar un número válido. ")     

    nuevo_pais = {
    "nombre": nombre_agregar,
    "poblacion": agregar_pob,
    "superficie": agregar_sup,
    "continente": continente}   
    # Agrega el nuevo país a la lista
    paises.append(nuevo_pais)

    print("País agregado correctamente.")


# ACTUALIZAR PAIS
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
        if nueva_pob <= 0 or nueva_sup <= 0:
            print("Error: Ingrese un valor mayor a 0.")
            return
    except ValueError:
        print("Error: Ingrese números válidos.")
        return

    # SE MODIFICAN LOS DATOS DENTRO DE LA LISTA
    paises[indice_encontrado]["poblacion"] = nueva_pob
    paises[indice_encontrado]["superficie"] = nueva_sup
    print(f"¡Datos de {pais['nombre']} modificados en la memoria!")


# BUSCAR PAIS
def buscar_pais(paises):
    print("\n--- BUSCAR PAÍS ---")

    buscar_nombre = input("Ingrese el nombre del país a buscar: ").strip()

    if buscar_nombre == "":
        print("Debe ingresar un nombre.")
        return

    pais_encontrado = False

    for pais in paises:
        # Busca coincidencias parciales ignorando mayúsculas y minúsculas
        if buscar_nombre.lower() in pais["nombre"].lower():

            print(f"""
Nombre: {pais["nombre"]}
Población: {pais["poblacion"]}
Superficie: {pais["superficie"]} km²
Continente: {pais["continente"]}
""")

            pais_encontrado = True

    if pais_encontrado == False:
        print("No se encontró ningún país.")


##############################################
# SUBMENU FILTRO
##############################################
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


#FUNCIONES SUBMENU FILTRO
# Mostrar únicamente los países que pertenecen al continente ingresado
def filtrar_por_continente(paises):
    continente = input("Ingrese el continente: ").strip()

    encontrado = False

    for pais in paises:

        if pais["continente"].lower() == continente.lower():

            print(f"""
Nombre: {pais["nombre"]}
Población: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}
""")

            encontrado = True

    if encontrado == False:
        print("No se encontraron países.")


# Mostrar países cuya población se encuentre dentro del rango indicado
def filtrar_por_poblacion(paises):
    try:

        minimo = int(input("Ingrese población mínima: "))
        maximo = int(input("Ingrese población máxima: "))

    except ValueError:
        print("Debe ingresar números enteros.")
        return

    encontrado = False

    for pais in paises:

        if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:

            print(f"""
Nombre: {pais["nombre"]}
Población: {pais["poblacion"]}
""")

            encontrado = True

    if encontrado == False:
        print("No se encontraron países.")


# Mostrar países cuya superficie se encuentre dentro del rango indicado
def filtrar_por_superficie(paises):
    try:

        minimo = int(input("Ingrese superficie mínima: "))
        maximo = int(input("Ingrese superficie máxima: "))

    except ValueError:
        print("Debe ingresar números enteros.")
        return

    encontrado = False

    for pais in paises:

        if pais["superficie"] >= minimo and pais["superficie"] <= maximo:

            print(f"""
Nombre: {pais["nombre"]}
Superficie: {pais["superficie"]}
""")

            encontrado = True

    if encontrado == False:
        print("No se encontraron países.")


##############################################
#SUBMENU ORDENAR
##############################################
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


#FUNCIONES SUBMENU ORDENAR
# Ordenamiento burbuja por nombre
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


# Ordenamiento burbuja por población
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


# Ordenamiento burbuja por superficie
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


##############################################
#SUBMENU MOSTRAR ESTADISTICAS
##############################################
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


#FUNCIONES MOSTRAR ESTADISTICAS
# Buscar el país con mayor población
def mayor_poblacion(paises):
    print("\n--- PAIS CON MAYOR POBLACION ---")

    mayor = paises [0]

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    print (f"""
Nombre: {mayor["nombre"]}
Población: {mayor["poblacion"]}
Continente: {mayor["continente"]}
""")


# Buscar el país con menor población
def menor_poblacion(paises):
    print("\n--- PAIS CON MENOR POBLACION ---")

    menor = paises [0]

    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
            
    print (f"""
Nombre: {menor["nombre"]}
Población: {menor["poblacion"]}
Continente: {menor["continente"]}
""")
    

# Sumar valores para calcular los promedios de la población y superficie
def promedios(paises):
    print("\n--- PROMEDIOS ---")

    total_poblacion = 0
    total_superficie = 0

    for pais in paises:

        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    print(f"""
Promedio de población: {promedio_poblacion:.2f}
Promedio de superficie: {promedio_superficie:.2f}
""")


# Contar cuántos países hay por continente
def cantidad_por_continente(paises):
    print("\n--- CANTIDAD DE PAÍSES POR CONTINENTE ---")

    cantidades = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in cantidades:

            cantidades[continente] += 1

        else:

            cantidades[continente] = 1

    for continente in cantidades:

        print(f"{continente}: {cantidades[continente]} países")


##############################################
#FUNCIONES AUXILIARES
##############################################
def mostrar_paises(paises): 
    print("\n =====PAISES=====")
    for pais in paises:
        print(pais["nombre"], "-", pais["continente"])


# Devuelve True si el país ya existe en la lista
def pais_duplicado(paises, nombre):
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True

    return False 


##############################################
#MENU_PRINCIPAL
##############################################
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