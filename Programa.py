# Bonaroti, Francisco 111
# Cosenza, Teo 107
# Gilardoni, Lucio 107
# Vacs, Francisco 107

import os
from select import select

global CAMIONES
CAMIONES = 0
global CAMIONES_SOJA
CAMIONES_SOJA = 0
global CAMIONES_MAIZ
CAMIONES_MAIZ = 0
global PESO_SOJA
PESO_SOJA = 0
global PESO_MAIZ
PESO_MAIZ = 0
global PROMEDIO_SOJA
PROMEDIO_SOJA = 0
global PROMEDIO_MAIZ
PROMEDIO_MAIZ = 0
global PATENTE_MAS_SOJA
PATENTE_MAS_SOJA = 0
global PATENTE_MAS_MAIZA
PATENTE_MAS_MAIZ = 0


def menu_principal():
    os.system("cls")
    print("MENU PRINCIPAL:")
    print("\t 1 - ADMINISTRACIONES")
    print("\t 2 - ENTREGA DE CUPOS")
    print("\t 3 - RECEPCION")
    print("\t 4 - REGISTRAR CALIDAD")
    print("\t 5 - REGISTRAR PESO BRUTO")
    print("\t 6 - REGISTRAR DESCARGA")
    print("\t 7 - REGISTRAR CARGA")
    print("\t 8 - REPORTES")
    print("\t 0 - FIN DEL PROGRAMA")


def menu_administraciones():
    os.system("cls")
    print("ADMINISTRACIONES")
    print("\t A- TITULARES")
    print("\t B- PRODUCTOS")
    print("\t C- RUBROS")
    print("\t D- RUBROS x PRODUCTO")
    print("\t E- SILOS")
    print("\t F- SUCURSALES")
    print("\t G- PRODUCTO POR TITULAR ")
    print("\t V- VOLVER AL MENU PRINCIPAL")
    select = input("OPCION DESEADA: \n").upper()
    if select == ("A" or "B" or "C" or "D" or "E" or "F" or "G"):
        menu_de_opciones()
    if select == "V":
        menu_principal()


def menu_de_opciones():
    os.system("cls")
    print("MENU DE OPCIONES ADMINISTRACIONES")
    print("\t A- ALTA")
    print("\t B- BAJA")
    print("\t C- CONSULTA")
    print("\t M- MODIFICACION")
    print("\t V- VOLVER AL MENU ANTERIOR")
    seleccionarda = input("OPCION DESEADA: \n").upper()
    if seleccionarda == ("A" or "B" or "C" or "M"):
        print("\t Esta funcionalidad esta en construccion\n")
        os.system("pause")
        menu_de_opciones()
    if seleccionarda == "V":
        menu_administraciones()


def menu_recepcion():
    global CAMIONES
    global CAMIONES_SOJA
    global PESO_SOJA
    global PATENTE_MAS_SOJA
    global CAMIONES_MAIZ
    global PESO_MAIZ
    global PATENTE_MAS_MAIZ

    os.system("cls")
    otro_Camion = "S"

    while otro_Camion != "N":
        print("SE HA RECIBIDO UN CAMION")
        patente = int(input("\t NUMERO DE PATENTE: "))
        CAMIONES = CAMIONES + 1

        print("OPCIONES DE CARGAMENTO:")
        print("\t 1 - SOJA")
        print("\t 2 - MAIZ")
        tipo_Cargamento = int(input())

        peso_bruto_temp = int(input("INGRESO PESO BRUTO: "))
        tara_temp = int(input("INGRESE SU TARA: "))
        neto_temp = peso_bruto_temp - tara_temp
        if tipo_Cargamento == 1:
            CAMIONES_SOJA += 1
            PESO_SOJA += neto_temp
            if PATENTE_MAS_SOJA < neto_temp:
                PATENTE_MAS_SOJA = neto_temp

        if tipo_Cargamento == 2:
            CAMIONES_MAIZ += 1
            PESO_MAIZ += neto_temp
            if PATENTE_MAS_MAIZ < neto_temp:
                PATENTE_MAS_MAIZ = neto_temp

        print("EL PESO NETO DEL CAMION " + str(CAMIONES) + " ES: ", neto_temp)

        otro_Camion = input("¿DESEA AGREGAR OTRO CAMION? (S/N)")


# programa main

seleccion = -1
while seleccion != 0:

    menu_principal()
    seleccion = int(input("SELECCIONAR OPCION: \n"))

    if seleccion == 1:
        menu_administraciones()

    if seleccion == (2 or 4 or 5 or 6 or 7):
        print("\t Esta funcionalidad esta en construccion\n")
        os.system("pause")

    if seleccion == 3:
        menu_recepcion()

    if seleccion == 8:
        os.system("cls")
        print("\nLA CANTIDAD TOTAL DE CAMIONES ES: ")
        print(CAMIONES)
        print("\nLA CANTIDAD TOTAL DE CAMIONES DE SOJA ES: ")
        print(CAMIONES_SOJA)
        print("\nLA CANTIDAD TOTAL DE CAMIONES DE MAÍZ ES: ")
        print(CAMIONES_MAIZ)
        print("\nEL PESO NETO TOTAL DE SOJA ES: ")
        print(PESO_SOJA)
        print("\nEL PESO NETO TOTAL DE MAÍZ ES: ")
        print(PESO_MAIZ)
        print("\nEL PROMEDIO DEL PESO NETO DE SOJA POR CAMIÓN ES: ")
        print(PROMEDIO_SOJA)
        print("\nEL PROMEDIO DEL PESO NETO DE MAIZ POR CAMIÓN ES: ")
        print(PROMEDIO_MAIZ)
        print("\nLA PATENTE DEL QUE MÁS SOJA DESCARGO ES: ")
        print(PATENTE_MAS_SOJA)
        print("\nLA PATENTE DEL QUE MÁS MAIZ DESCARGO ES: ")
        print(PATENTE_MAS_MAIZ)
        os.system("pause")

    if seleccion == 0:
        print("FIN DEL PROGRAMA")
