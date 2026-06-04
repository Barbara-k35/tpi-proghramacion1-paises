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
        archivo.close
    

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV")

    return paises


##############################################
#FUNCIONES PRINCIPALES
#AGREGAR_PAISES
def agregar_pais(paises):
    pass

#ACTUALIZAR_PAISES
def actualizar_pais(paises):
    pass

#BUSCAR_PAIS
def buscar_pais(paises):
    pass


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
    pass
def ordenar_por_poblacion(paises):
    pass
def ordenar_por_superficie(paises):
    pass


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
                print("test op1")

            elif opcion == 2:
               print("test op2")

            elif opcion == 3:
                print("test op3")

            elif opcion == 4:
                filtrar_paises(paises)

            elif opcion == 5:
                ordenar_paises(paises)

            elif opcion == 6:
                print("test op 6")

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