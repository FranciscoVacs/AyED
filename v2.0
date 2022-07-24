# Bonaroti, Francisco 111
# Cosenza, Teo 107
# Gilardoni, Lucio 107
# Vacs, Francisco 107

import os

def menu_principal():
    os.system("cls")
    print("MENU PRINCIPAL:")
    print("\t 1 - ADMINISTRACIONES")
    print("\t 2 - ENTREGA DE CUPOS")
    print("\t 3 - RECEPCION")
    print("\t 4 - REGISTRAR CALIDAD")
    print("\t 5 - REGISTRAR PESO BRUTO")
    print("\t 6 - REGISTRAR DESCARGA")
    print("\t 7 - REGISTRAR TARA")
    print("\t 8 - REPORTES")
    print("\t 0 - FIN DEL PROGRAMA")


def menu_administraciones(cargados): #cargados:array[2] de string[6]
    seleccion = "" #char
    while seleccion != "V":
        while seleccion not in ("A", "B", "C", "D", "E", "F", "G", "V"):
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
            seleccion = input("Seleccione una opcion: ").upper()
            if seleccion not in ("A", "B", "C", "D", "E", "F", "G", "V"):
                print("No existe la opcion\n")
                os.system("pause")
                seleccion = ""
        if seleccion != "V":
            menu_opciones(seleccion, cargados)
            seleccion = ""


def menu_opciones(x, cargados): #x:char; cargados:array[2] de string[6]
    seleccion = "" #char
    while seleccion != "V":
        while seleccion not in ("A", "B", "C", "M", "V"):
            os.system("cls")
            print("OPCIONES")
            print("\t A - ALTA")
            print("\t B - BAJA")
            print("\t C - CONSULTA")
            print("\t M - MODIFICACION")
            print("\t V - VOLVER")
            seleccion = input("Seleccione una opcion: ").upper()
            if seleccion not in ("A", "B", "C", "M", "V"):
                print("No existe la opcion\n")
                os.system("pause")
            if seleccion != "V":
                if x == "B":
                    edicion(seleccion, cargados)
                else:
                    print("Esta funcionalidad esta en construccion\n")
                    os.system("pause")
                seleccion = ""


def edicion(x, cargados): #x:char; cargados:array[2] de string[6]
    productos = ["SOJA", "TRIGO", "MAIZ", "GIRASOL", "CEBADA"] #array[4] de string[6]
    prod_elegido = "" #string[6]
    not_repe = 1 #int
    usado=False #boolean
    match x:

        case "A":
            if "" not in cargados:
                print("Los tres estan llenos, borra o modifica uno")
                os.system("pause")
            else:
                while prod_elegido not in productos:
                    os.system("cls")
                    print("PRODUCTOS")
                    print(productos)
                    prod_elegido = input("Producto a cargar: ").upper()
                    if prod_elegido not in productos:
                        print("El producto ingresado no existe")
                        os.system("pause")
                i = 0 #int
                while i < 3 and cargados[i] != prod_elegido:
                    i += 1
                if i < 3:
                    print("El producto ya está cargado")
                    os.system("pause")
                    not_repe = 0
                i = 0
                while cargados[i] != "":
                    i += 1
                if not_repe:
                    cargados[i] = prod_elegido

        case "B":
            if cargados[0] == "" and cargados[1] == "" and cargados[2] == "":
                os.system("cls")
                print("Todavia no se cargo ningun producto")
                os.system("pause")
            else:
                while prod_elegido not in productos:
                    os.system("cls")
                    print(cargados)
                    prod_elegido = input("Ingrese el producto a eliminar: ").upper()
                    if prod_elegido not in cargados:
                        print("Lo ingresado no es un producto cargado")
                        os.system("pause")
                    i=0
                    while i<8 and prod_elegido!=camiones[i][1]:
                        i+=1
                    if i<8:
                        usado=True
                        print("No se puede eliminar porque el producto esta en uso")
                        os.system("pause")
                i = 0
                while prod_elegido != cargados[i]:
                    i += 1
                if usado==False:
                    cargados[i] = ""

        case "C":
            if cargados[0] == "" and cargados[1] == "" and cargados[2] == "":
                os.system("cls")
                print("Todavia no se cargo ningun producto")
                os.system("pause")
            else:
                os.system("cls")
                print(cargados)
                os.system("pause")

        case "M":
            if cargados[0] == "" and cargados[1] == "" and cargados[2] == "":
                os.system("cls")
                print("Todavia no se cargo ningun producto")
                os.system("pause")
            else:
                prod_sacar = " " #string[6]
                prod_nuevo = " " #string[6]
                while prod_sacar not in cargados:
                    os.system("cls")
                    print(cargados)
                    prod_sacar = input("Ingrese el producto a modificar: ").upper()
                    if prod_sacar not in cargados:
                        print("El producto ingresado no esta cargado")
                        os.system("pause")
                i=0 #int
                while i<8 and prod_sacar!=camiones[i][1]:
                    i+=1
                if i<8:
                    usado=True
                    print("No se puede modificar porque el producto esta en uso")
                    os.system("pause")
                if usado==False:
                    while prod_nuevo not in productos or prod_nuevo in cargados:
                        os.system("cls")
                        print(productos)
                        prod_nuevo = input("Ingrese el nuevo producto: ").upper()
                        if prod_nuevo not in productos and prod_nuevo in cargados:
                            print("El producto ingresado no corresponde")
                    i = 0
                    while prod_sacar != cargados[i]:
                        i += 1
                    cargados[i] = prod_nuevo


def entrega_cupos(camiones, estado, cargados):
    os.system("cls")
    if cargados[0] == "" and cargados[1] == "" and cargados[2] == "":
        print("Todavia no se cargo ningun producto, cargue uno y vuelva")
        os.system("pause")
    else:
        otro = True #boolean
        while otro:
            otro = False
            i = 0
            while i < 8 and camiones[i][0] != "":  # se fija que haya uno vacio y donde
                i += 1
            if i < 8:  # si hay uno vacio
                libre = i #int
                new_patente = "" #string
                while (len(new_patente) < 6 or len(new_patente) > 7):
                    new_patente = input("Ingrese la nueva patente: ")
                    if len(new_patente) < 6 or len(new_patente) > 7:
                        print("Patente no aceptada")
                        os.system("pause")
                i = 0
                while new_patente != camiones[i][0] and camiones[i][0] != "":  # chequea q no repita hasta la 1ra vacia
                    i += 1
                if camiones[i][0] == "":
                    i = 0
                    producto = "" #string
                    productos = ["SOJA", "TRIGO", "MAIZ", "GIRASOL", "CEBADA"] #array[5] de string[7]
                    while producto not in productos:
                        producto = input("Ingrese el producto transportado: ")
                        if producto not in productos:
                            print("Producto no reconocido")
                            os.system("pause")
                    if producto not in cargados:
                        print("Producto no cargado, cargue y vuelva")
                        os.system("pause")
                    else:
                        camiones[libre][1] = producto
                        camiones[libre][0] = new_patente
                        estado[libre] = 'P'

                else:
                    print("Patente ya ingresada")
                    os.system("pause")
                rta = "" #char
                while rta != "S" and rta != "N":
                    rta = input("Obtener otro cupo? S/N: ").upper()
                    if rta != "S" and rta != "N":
                        print("Rta no aceptada")
                        os.system("pause")
                if rta == "S":
                    otro = True
            else:
                print("No quedan cupos disponibles")
                os.system("pause")
    if cargados[0]!="" or cargados[1]!="" or cargados[2]!="":
        return libre + 1
    else:
        return 0


def menu_recepcion(camiones, estado): #camiones: array[1] de string[6]; estado:char
    os.system("cls")
    new_patente = "" #string[6]
    while new_patente!="*":
        while (len(new_patente) < 6 or len(new_patente) > 7) and new_patente != "*":
            new_patente = input("Ingrese la nueva patente (* para finalizar): ")
            if (len(new_patente) < 6 or len(new_patente) > 7) and new_patente != "*":
                print("Patente no aceptada")
                os.system("pause")
        if new_patente != "*":
            i = 0 #int
            while i < 8 and camiones[i][0] != new_patente:
                i += 1
            if i == 8:
                print("Patente sin cupo")
                os.system("pause")
            elif estado[i] != 'P':
                print("Patente ya recibida")
                os.system("pause")
            else: 
                estado[i] = 'E'
            new_patente = ""


def registro_pb(camiones, estado, pesos): #camiones: array[1] de string[6]; estado:char; pesos: array[2] de int
    os.system("cls")
    if camiones[0][0] != "":
        patente = "" #string[6]
        while len(patente) < 6 or len(patente) > 7:
            patente = input("Ingrese la patente del camion: ")
            if len(patente) < 6 or len(patente) > 7:
                print("Patente no aceptada")
                os.system("pause")
        i = 0 #int
        while i < 8 and patente != camiones[i][0]:
            i += 1
        if i < 8 and pesos[i][0]==0:
            if estado[i] == 'E' and pesos[i][0] == 0:
                pesos[i][0] = int(input("Ingrese el peso bruto del camion: "))
            elif estado[i] != 'E':
                print("El camion no fue recibido")
                os.system("pause")
        else:
            print("El peso bruto de este camion ya fue registrado")
            os.system("pause")
    else:
        print("Todavia no se asigno ningun cupo")
        os.system("pause")


def registro_tara(camiones, estado, pesos): #camiones: array[1] de string[6]; estado:char; pesos: array[2] de int
    os.system("cls")
    if camiones[0][0] != "":
        patente = "" #string[6]
        while len(patente) < 6 or len(patente) > 7:
            patente = input("Ingrese la patente del camion: ")
            if len(patente) < 6 or len(patente) > 7:
                print("Patente no aceptada")
                os.system("pause")
        i = 0 #int
        while i < 8 and patente != camiones[i][0]:
            i += 1
        if i < 8 and pesos[i][1]==0:
            pesos[i][1] = pesos[i][0]
            if estado[i] == 'E' and pesos[i][0] != 0 and pesos[i][1] == pesos[i][0]:
                while pesos[i][1] >= pesos[i][0]:
                    pesos[i][1] = int(input("Ingrese la tara del camion: "))
                    if pesos[i][1] >= pesos[i][0]:
                        print("La tara debe ser menor o igual al peso bruto")
                        os.system("pause")
                estado[i] = 'C'
                pesos[i][2] = pesos[i][0] - pesos[i][1]
            elif estado[i] != 'E':
                print("El camion no fue recibido")
                os.system("pause")
            elif pesos[i][0] == 0:
                print("Previamente se debe registrar el peso bruto")
                os.system("pause")
        else:
            print("La tara de este camion ya fue registrado")
            os.system("pause")
    else:
        print("Todavia no se asigno ningun cupo")
        os.system("pause")


def reportes(cupos, estado, camiones, pesos, cargados):#cupos: int; estado:char; camiones:array[1] de string[6]; pesos: array[2] de int; cargados: array[2] de string[6]
    os.system("cls")
    print("Se entregaron " + str(cupos) + " cupos")
    i = 0 #int
    recibidos = 0 #int
    camiones_prod = [0] * 3 #array[2] de string[7]
    pesos_netos = [0] * 3 #array[2] de int

    while i < 8:
        if estado[i] == 'E' or estado[i] == 'C':
            recibidos += 1
        if camiones[i][0] != "" and camiones[i][1] == cargados[0]:
            camiones_prod[0] += 1
            pesos_netos[0] += pesos[i][2]
        if camiones[i][0] != "" and camiones[i][1] == cargados[1]:
            camiones_prod[1] += 1
            pesos_netos[1] += pesos[i][2]
        if camiones[i][0] != "" and camiones[i][1] == cargados[2]:
            camiones_prod[2] += 1
            pesos_netos[2] += pesos[i][2]
        i += 1

    print("Se recibieron " + str(recibidos) + " camiones")

    if recibidos > 1:
        for i in range(3):
            if cargados[i] != "":
                if camiones_prod[i] > 0:
                    print("Hay " + str(camiones_prod[i]) + " camiones de " + cargados[i])
                    print("Peso neto promedio de " + cargados[i] + ": " + str(pesos_netos[i] / camiones_prod[i]))
                    j = 0 #int
                    neto_max = 0 #int
                    patente_max = "" #string[6]
                    while j < 8:
                        if camiones[j][1] == cargados[i] and neto_max <= pesos[j][2]:
                            neto_max = pesos[j][2]
                            patente_max = camiones[j][0]
                        j+=1
                    print("Patente que más " + cargados[i] + " trajo: " + patente_max)
                    j = 0
                    neto_min = neto_max #int
                    patente_min = patente_max #string[6]
                    while j < 8:
                        if camiones[j][1] == cargados[i] and neto_min >= pesos[j][2]:
                            neto_min = pesos[j][2]
                            patente_min = camiones[j][0]
                        j+=1
                    print("Patente que menos " + cargados[i] + " trajo: " + patente_min)
                print("Peso neto de " + cargados[i] + ": " + str(pesos_netos[i]))
        for i in range(recibidos - 1):
            j = i + 1
            while j <= recibidos:
                if pesos[i][2] < pesos[j][2]:
                    for k in range(3):
                        aux_pesos = pesos[i][k]
                        pesos[i][k] = pesos[j][k]
                        pesos[j][k] = aux_pesos
                    for k in range(2):
                        aux_camiones = camiones[i][k]
                        camiones[i][k] = camiones[j][k]
                        camiones[j][k] = aux_camiones
                j += 1
        print("LISTADO ORDENADO POR PESO NETO: ")
        for i in range(recibidos):
            print(camiones[i][0] + '\t' + camiones[i][1] + '\t' + str(pesos[i][2]))
    elif recibidos == 1:
        print("LISTADO ORDENADO POR PESO NETO: ")
        print(camiones[0][0] + '\t' + camiones[0][1] + '\t' + str(pesos[0][2]))
    os.system("pause")


# programa main

cargados = [""] * 3 #array[2] de string[6]
camiones = [""] * 8 #array[7][2] de string[6] 
for i in range(8):
    camiones[i] = [""] * 2
estado = ["-"] * 8 #array[7] de char
pesos = [0] * 8 #array[7][2] de int
for i in range(8):
    pesos[i] = [0] * 3
cupos = 0 #int

seleccion = "-" #char
while seleccion != "0":
    menu_principal()
    seleccion = input("Seleccione una opcion: ")

    if seleccion == "1":
        menu_administraciones(cargados)

    elif seleccion == "2":
        cupos = entrega_cupos(camiones, estado, cargados[:])

    elif seleccion in ("4", "6"):
        print("Esta funcionalidad esta en construccion\n")
        os.system("pause")

    elif seleccion == "3":
        menu_recepcion(camiones[:], estado)

    elif seleccion == "5":
        registro_pb(camiones[:], estado[:], pesos)

    elif seleccion == "7":
        registro_tara(camiones[:], estado[:], pesos)

    elif seleccion == "8":
        reportes(cupos, estado[:], camiones[:], pesos[:], cargados[:])

    elif seleccion == "0":
        print("FIN DEL PROGRAMA")

    else:
        print("Opcion incorrecta, seleccione otra")
        os.system("pause")
