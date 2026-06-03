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
    pass

#FUNCIONES_SUBMENU_FILTRO

#SUBMENU_ORDENAR
def ordenar_paises(paises):
    pass

#FUNCIONES_SUBMENU_ORDENAR

#SUBMENU_MOSTRAR_ESTADISTICAS
def mostrar_estadisticas(paises):
    pass

#FUNCIONES_MOSTRAR_ESTADISTICAS


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
                print("test op4")

            elif opcion == 5:
                print("test op 5")

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