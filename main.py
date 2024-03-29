# Bonaroti, Francisco 111
# Cosenza, Teo 107
# Gilardoni, Lucio 107
# Vacs, Francisco 107

import os

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
PATENTE_MAS_SOJA = "-"
global PATENTE_MAS_MAIZ
PATENTE_MAS_MAIZ = "-"


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
    select = input("Seleccione una opcion: ").upper()
    if select in ("A", "B", "C", "D", "E", "F", "G"):
        menu_de_opciones()
    elif select == "V":
        menu_principal()
    else:
        print("Opcion incorrecta, seleccione otra..")
        os.system("pause")
        menu_administraciones()


def menu_de_opciones():
    os.system("cls")
    print("MENU DE OPCIONES ADMINISTRACIONES")
    print("\t A- ALTA")
    print("\t B- BAJA")
    print("\t C- CONSULTA")
    print("\t M- MODIFICACION")
    print("\t V- VOLVER AL MENU ANTERIOR")
    selec = input("Seleccione una opcion: ").upper()
    if selec in ("A", "B", "C", "M"):
        print("Esta funcionalidad esta en construccion\n")
        os.system("pause")
        menu_de_opciones()
    elif selec == "V":
        menu_administraciones()
    else:
        print("Opcion incorrecta, seleccione otra..")
        os.system("pause")
        menu_de_opciones()


def menu_recepcion():
    global CAMIONES
    global CAMIONES_SOJA
    global PESO_SOJA
    global PATENTE_MAS_SOJA
    global CAMIONES_MAIZ
    global PESO_MAIZ
    global PATENTE_MAS_MAIZ
    global PROMEDIO_SOJA
    global PROMEDIO_MAIZ

    os.system("cls")
    otro_Camion = "-"
    mayor_soja = 0
    mayor_maiz = 0
    tipo_Cargamento = "-"
    peso_bruto_temp = 0
    tara_temp = 0

    while otro_Camion != "N":
        os.system("cls")
        print("\nSE HA RECIBIDO UN CAMION")
        patente = input("\t NUMERO DE PATENTE: ")
        CAMIONES = CAMIONES + 1

        while tipo_Cargamento != "1" and tipo_Cargamento != "2":
            print("\nOPCIONES DE CARGAMENTO:")
            print("\t 1 - SOJA")
            print("\t 2 - MAIZ")
            tipo_Cargamento = input("\nSeleccion: ")
            if tipo_Cargamento != "1" and tipo_Cargamento != "2":
                print("\nRespuesta no aceptada. Vuelva a intentarlo.\n")

        while peso_bruto_temp <= 0:
            peso_bruto_temp = float(input("\nINGRESE PESO BRUTO: "))
            if peso_bruto_temp <= 0:
                print("\nDebe ingresar un valor adecuado.\n")

        while tara_temp <= 0 or tara_temp > peso_bruto_temp:
            tara_temp = float(input("\nINGRESE SU TARA: "))
            if tara_temp <= 0:
                print("\nDebe ingresar un valor adecuado.\n")
            if tara_temp > peso_bruto_temp:
                print("\nDebe ingresar una tara meno al peso bruto.\n")

        neto_temp = peso_bruto_temp - tara_temp

        if tipo_Cargamento == "1":
            global CAMIONES_SOJA
            CAMIONES_SOJA = CAMIONES_SOJA + 1
            PESO_SOJA = PESO_SOJA + neto_temp
            if mayor_soja < neto_temp:
                PATENTE_MAS_SOJA = patente
                mayor_soja = neto_temp

        if tipo_Cargamento == "2":
            CAMIONES_MAIZ = CAMIONES_MAIZ + 1
            PESO_MAIZ = PESO_MAIZ + neto_temp
            if mayor_maiz < neto_temp:
                PATENTE_MAS_MAIZ = patente
                mayor_maiz = neto_temp

        print("\nEL PESO NETO DEL CAMION " + str(CAMIONES) + " ES: ", neto_temp)
        while otro_Camion != "S" and otro_Camion != "N":
            otro_Camion = input("\n¿DESEA AGREGAR OTRO CAMION? (S/N)\n").upper()
            if otro_Camion != "S" and otro_Camion != "N":
                print("\nRespuesta no aceptada.\n")

        if otro_Camion == "S":
            tipo_Cargamento = "-"
            peso_bruto_temp = 0
            tara_temp = 0
            otro_Camion = "-"

    if CAMIONES_MAIZ > 0:
        PROMEDIO_MAIZ = PESO_MAIZ / CAMIONES_MAIZ
    if CAMIONES_SOJA > 0:
        PROMEDIO_SOJA = PESO_SOJA / CAMIONES_SOJA


def reportes():
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


# programa main

seleccion = "-"
while seleccion != "0":

    menu_principal()
    seleccion = input("Seleccione una opcion: ")

    if seleccion == "1":
        menu_administraciones()

    elif seleccion in ("2", "4", "5", "6", "7"):
        print("Esta funcionalidad esta en construccion\n")
        os.system("pause")

    elif seleccion == "3":
        menu_recepcion()

    elif seleccion == "8":
        reportes()

    elif seleccion == "0":
        print("FIN DEL PROGRAMA")

    else:
        print("Opcion incorrecta, seleccione otra")
        os.system("pause")
        menu_principal()
