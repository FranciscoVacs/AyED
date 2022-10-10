# Bonaroti, Francisco 111
# Cosenza, Teo 107
# Gilardoni, Lucio 107
# Vacs, Francisco 107

import os
import os.path
import pickle
from datetime import datetime
from datetime import date


class Operacion:
    def __init__(self):
        self.patente = ""
        self.cod = 0
        self.fecha_cupo = ""
        self.estado = ''
        self.bruto = 0
        self.tara = 0


class Producto:
    def __init__(self):
        self.cod = 0
        self.nombre = ""
        self.cargado = True


class Rubro:
    def __init__(self):
        self.cod = 0
        self.nombre = ""


class Rubro_prod:
    def __init__(self):
        self.cod_rubro = 0
        self.cod_prod = 0
        self.min = 0.0
        self.max = 0.0


class Silo:
    def __init__(self):
        self.cod_silo = 0
        self.nombre = ""
        self.cod_prod = 0
        self.stock = 0


class Promedio:
    def __int__(self):
        self.nombre = ""
        self.total = 0
        self.div = 0


global AL_RubroProds, AF_RubroProds
global AL_Silos, AF_Silos
global AL_Rubros, AF_Rubros
global AL_Prods, AF_Prods
global AL_Ops, AF_Ops
global AL_Cupos


def archivos():
    global AL_RubroProds, AF_RubroProds
    global AL_Silos, AF_Silos
    global AL_Rubros, AF_Rubros
    global AL_Prods, AF_Prods
    global AL_Ops, AF_Ops
    global AL_Cupos
    AF_RubroProds = "rubro_prods.dat"
    if not os.path.exists(AF_RubroProds):
        AL_RubroProds = open(AF_RubroProds, "w+b")
    else:
        AL_RubroProds = open(AF_RubroProds, "r+b")

    AF_Silos = "silos.dat"
    if not os.path.exists(AF_Silos):
        AL_Silos = open(AF_Silos, "w+b")
    else:
        AL_Silos = open(AF_Silos, "r+b")

    AF_Rubros = "rubros.dat"
    if not os.path.exists(AF_Rubros):
        AL_Rubros = open(AF_Rubros, "w+b")
    else:
        AL_Rubros = open(AF_Rubros, "r+b")

    AF_Prods = "productos.dat"
    if not os.path.exists(AF_Prods):
        AL_Prods = open(AF_Prods, "w+b")
    else:
        AL_Prods = open(AF_Prods, "r+b")

    AF_Ops = "operaciones.dat"
    if not os.path.exists(AF_Ops):
        AL_Ops = open(AF_Ops, "w+b")
    else:
        AL_Ops = open(AF_Ops, "r+b")

    AF_Cupos = "cupos.dat"
    if not os.path.exists(AF_Cupos):
        AL_Cupos = open(AF_Cupos, "w+b")
        temp = 0
        pickle.dump(temp, AL_Cupos)
        AL_Cupos.flush()
    else:
        AL_Cupos = open(AF_Cupos, "r+b")


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
    print("\t 9 - LISTADO DE SILOS Y RECHAZOS")
    print("\t 0 - FIN DEL PROGRAMA")


def menu_administraciones():  # cargados:array[2] de string[6]
    seleccion = ""  # char
    posibles = ["A", "B", "C", "D", "E", "F", "G", "V"]
    pertenece = -1
    while seleccion != "V":
        while pertenece == -1:
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
            pertenece = busq_Sec_1D(posibles[:], seleccion)
            if pertenece == -1:
                print("No existe la opcion\n")
                os.system("pause")
                seleccion = ""
        if seleccion != "V":
            construc = ["A", "F", "G"]
            if busq_Sec_1D(construc[:], seleccion) != -1:
                print("Esta funcionalidad esta en construcción")
                os.system("pause")
                os.system("cls")
            else:
                menu_opciones(seleccion)
            seleccion = ""
            pertenece = -1


def menu_opciones(x):  # x:char; cargados:array[2] de string[6]
    seleccion = ""  # char
    posibles = ["A", "B", "C", "M", "V"]
    pertenece = -1
    while seleccion != "V":
        while pertenece == -1:
            os.system("cls")
            print("OPCIONES")
            print("\t A - ALTA")
            print("\t B - BAJA")
            print("\t C - CONSULTA")
            print("\t M - MODIFICACION")
            print("\t V - VOLVER")
            seleccion = input("Seleccione una opcion: ").upper()
            pertenece = busq_Sec_1D(posibles[:], seleccion)
            if pertenece == -1:
                print("No existe la opcion\n")
                os.system("pause")
            elif seleccion != "V":
                pertenece = -1
                if x == "B":
                    match seleccion:
                        case "A":
                            altaProds()
                        case "B":
                            baja()
                        case "C":
                            consulta()
                        case "M":
                            modificacion()
                else:
                    match x:
                        case "C":
                            if seleccion == "A":
                                altaRubros()
                            else:
                                print("Esta funcionalidad esta en construcción")
                                os.system("pause")
                                os.system("cls")
                        case "D":
                            if seleccion == "A":
                                altaRxP()
                            else:
                                print("Esta funcionalidad esta en construcción")
                                os.system("pause")
                                os.system("cls")
                        case "E":
                            if seleccion == "A":
                                altaSilos()
                            else:
                                print("Esta funcionalidad esta en construcción")
                                os.system("pause")
                                os.system("cls")


def verifInt(x, min, max):
    try:
        x = int(x)
        if x < min or x > max:
            print("Error")
            os.system("pause")
            os.system("cls")
            return False
        else:
            return True
    except:
        os.system("cls")
        print("Se debe ingresar un numero entero")
        return False


def busqCod(cod, x):
    global AL_RubroProds, AF_RubroProds
    global AL_Rubros, AF_Rubros
    global AL_Prods, AF_Prods
    global AL_Ops, AF_Ops
    match x:
        case "B":
            AF_Aux = AF_Prods
            AL_Aux = AL_Prods
        case "C":
            AF_Aux = AF_Rubros
            AL_Aux = AL_Rubros
    t = os.path.getsize(AF_Aux)
    AL_Aux.seek(0)
    while AL_Aux.tell() < t:
        pos = AL_Aux.tell()
        aux = pickle.load(AL_Aux)
        if int(aux.cod) == cod:
            return pos
    return -1


def algunActivo():
    global AL_Prods, AF_Prods
    t = os.path.getsize(AF_Prods)
    AL_Prods.seek(0)
    while AL_Prods.tell() < t:
        aux = pickle.load(AL_Prods)
        if aux.cargado:
            return True
    return False


def altaProds():
    global AL_Prods, AF_Prods
    isInt = False
    cod = -1
    reg = Producto()
    while cod != 0:
        while not isInt:
            cod = input("Ingrese el código del nuevo producto (0 para salir, Max: 99999): ")
            isInt = verifInt(cod, 0, 99999)
        cod = int(cod)
        if cod != 0:
            pos = busqCod(cod, "B")
            if pos == -1:
                reg.cod = str(cod).ljust(5)
                reg.nombre = input("Ingrese el producto a cargar: ").upper()
                while len(reg.nombre) > 22 and len(reg.nombre) < 1:
                    print("Rta no aceptada, intente nuevamente")
                    os.system("pause")
                    os.system("cls")
                    reg.nombre = input("Ingrese el producto a cargar: ").upper()
                reg.nombre = reg.nombre.ljust(22)
                pickle.dump(reg, AL_Prods)
                AL_Prods.flush()
            else:
                AL_Prods.seek(pos)
                reg = pickle.load(AL_Prods)
                if reg.cargado:
                    print("Producto ya ingresado")
                    os.system("pause")
                else:
                    AL_Prods.seek(pos)
                    reg.cargado = True
                    pickle.dump(reg, AL_Prods)
                    AL_Prods.flush()
                    print("Se volvió a cargar el producto")
                    os.system("pause")
            isInt = False


def altaRubros():
    global AL_Rubros, AF_Rubros
    isInt = False
    cod = -1
    reg = Rubro()
    while cod != 0:
        while not isInt:
            cod = input("Ingrese el código del nuevo rubro (0 para salir, Max: 99999): ")
            isInt = verifInt(cod, 0, 99999)
        cod = int(cod)
        if cod != 0:
            pos = busqCod(cod, "C")
            if pos == -1:
                reg.cod = str(cod).ljust(5)
                reg.nombre = input("Ingrese el rubro a cargar: ").upper()
                while len(reg.nombre) > 22 and len(reg.nombre) < 1:
                    print("Rta no aceptada, intente nuevamente")
                    os.system("pause")
                    os.system("cls")
                    reg.nombre = input("Ingrese el rubro a cargar: ").upper()
                reg.nombre = reg.nombre.ljust(22)
                pickle.dump(reg, AL_Rubros)
                AL_Rubros.flush()
            else:
                print("Rubro ya ingresado")
                os.system("pause")
            isInt = False


def busqSilos(cod, tipo):
    global AL_Silos, AF_Silos
    t = os.path.getsize(AF_Silos)
    AL_Silos.seek(0)
    while AL_Silos.tell() < t:
        pos = AL_Silos.tell()
        aux = pickle.load(AL_Silos)
        match tipo:
            case "silo":
                if int(aux.cod_silo) == cod:
                    return pos
            case "prod":
                if int(aux.cod_prod) == cod:
                    return pos
    return -1


def altaSilos():
    global AL_Prods, AF_Prods
    if os.path.getsize(AF_Prods) == 0:  # tmb ver si estan todos dados de baja
        os.system("cls")
        print("Todavia no se cargo ningun producto")
        os.system("pause")
    else:
        global AL_Silos, AF_Silos
        reg = Silo()
        isInt = False
        cod = -1
        while cod != 0:
            while not isInt:
                cod = input("Ingrese el código del nuevo silo (0 para salir, Max: 99999): ")
                isInt = verifInt(cod, 0, 99999)
            cod = int(cod)
            if cod != 0:
                pos = busqSilos(cod, "silo")
                if pos == -1:
                    reg.cod_silo = str(cod).ljust(5)
                    reg.nombre = input("Ingrese el silo a cargar: ").upper()
                    while len(reg.nombre) > 22 and len(reg.nombre) < 1:
                        print("Rta no aceptada, intente nuevamente")
                        os.system("pause")
                        os.system("cls")
                        reg.nombre = input("Ingrese el silo a cargar: ").upper()
                    reg.nombre = reg.nombre.ljust(22)
                    #  Ingreso cod prod
                    pos = 0
                    isInt = False
                    while not isInt and pos != -1:
                        codP = input("Ingrese el código del producto correspondiente al silo: ")
                        isInt = verifInt(codP, 1, 99999)
                        codP = int(codP)
                        pos = busqCod(codP, "B")
                        if pos != -1:
                            if busqSilos(codP, "prod") == -1:
                                reg.cod_prod = str(codP).ljust(5)
                                pickle.dump(reg, AL_Silos)
                                AL_Silos.flush()
                                print("Silo cargado")
                                os.system("pause")
                                os.system("cls")
                            else:
                                print(" Ya se ingresó un silo de ese producto")
                                os.system("pause")
                        else:  # Refinar busqCod para q no incluya inactivos (agregar otra f(x))
                            print(" El código ingresado no corresponde con ningún producto cargado")
                else:
                    print(" Silo ya ingresado")
                    os.system("pause")
                isInt = False


def busqRxP(codR, codP):
    global AL_RubroProds, AF_RubroProds
    t = os.path.getsize(AF_RubroProds)
    AL_RubroProds.seek(0)
    while AL_RubroProds.tell() < t:
        pos = AL_RubroProds.tell()
        aux = pickle.load(AL_RubroProds)
        if int(aux.cod_prod) == codP and int(aux.cod_rubro) == codR:
            return pos
    return -1


def altaRxP():
    global AL_RubroProds, AF_RubroProds
    global AF_Rubros, AF_Prods
    if os.path.getsize(AF_Rubros) == 0 or os.path.getsize(AF_Prods) == 0 or not algunActivo():  # tmb ver si estan todos dados de baja
        os.system("cls")
        print("Todavía no se cargó ningún rubro y/o producto")
        os.system("pause")
    else:
        isInt = False
        cod = -1
        reg = Rubro_prod()
        while not isInt:
            codR = input("Ingrese el código del rubro: ")
            isInt = verifInt(codR, 1, 99999)
        isInt = False
        codR = int(codR)
        pos = busqCod(codR, "C")
        if pos != -1:
            while not isInt:
                codP = input("Ingrese el código del producto: ")
                isInt = verifInt(codP, 1, 99999)
            codP = int(codP)
            pos = busqCod(codP, "B")
            AL_Prods.seek(pos)
            aux = pickle.load(AL_Prods)
            if busqRxP(codR, codP) == -1:
                codP = str(codP).ljust(5)
                codR = str(codR).ljust(5)
                if pos != -1 and aux.cargado:
                    reg.cod_rubro = codR
                    reg.cod_prod = codP
                    isFloat = False
                    while not isFloat:
                        min = input("Ingrese el valor mínimo: ")
                        isFloat = verifFloat(min, 0, 100)
                    isFloat = False
                    min = int(min)
                    while not isFloat:
                        max = input("Ingrese el valor máximo: ")
                        isFloat = verifFloat(max, min, 100)
                    reg.min = str(min).ljust(8)
                    reg.max = str(max).ljust(8)
                    pickle.dump(reg, AL_RubroProds)
                    AL_RubroProds.flush()
                else:
                    print("Producto no ingresado")
                    os.system("pause")
            else:
                print("Ya se ingresó ese rubro para ese producto")
                os.system("pause")
        else:
            print("Rubro no ingresado")
            os.system("pause")


def verifFloat(x, min, max):
    try:
        x = float(x)
        if x < min or x > max:
            print("Error")
            os.system("pause")
            os.system("cls")
            return False
        else:
            return True
    except:
        os.system("cls")
        print("Se debe ingresar un número real")
        return False


def baja():  # verificar q no se este usando
    global AL_Prods, AF_Prods
    if os.path.getsize(AF_Prods) == 0 or not algunActivo():
        os.system("cls") 
        print("Todavia no se cargo ningun producto")
        os.system("pause")
    else:
        os.system("cls")
        reg = Producto()
        isInt = False
        cod = -1
        while cod != 0:
            while not isInt:
                cod = input("Ingrese el código del producto a eliminar (0 para salir): ")
                isInt = verifInt(cod, 0, 99999)
            cod = int(cod)
            if cod != 0:
                pos = busqCod(cod, "B")
                if pos == -1:
                    print("El codigo ingresado no existe")
                    os.system("pause")
                elif reg.cargado:
                    AL_Prods.seek(pos)
                    reg = pickle.load(AL_Prods)
                    AL_Prods.seek(pos)
                    reg.cargado = False
                    pickle.dump(reg, AL_Prods)
                    AL_Prods.flush()
                else:
                    print("El producto no está cargado")
                    os.system("pause")
                isInt = False


def consulta():
    if os.path.getsize(AF_Prods) == 0 or not algunActivo():
        os.system("cls")
        print("Todavía no se cargó ningún producto")
        os.system("pause")
    else:
        os.system("cls")
        print("----------------------------")
        print("| PRODUCTOS:")
        size = os.path.getsize(AF_Prods)
        AL_Prods.seek(0, 0)
        while AL_Prods.tell() < size:
            reg = pickle.load(AL_Prods)
            if reg.cargado:
                print("----------------------------")
                print("| Código: " + '\t' + str(reg.cod))
                print("| Nombre: " + '\t' + reg.nombre)
                print("| Estado: " + '\t' + str(reg.cargado))
        print("----------------------------")
        os.system("pause")


def modificacion():
    global AL_Prods, AF_Prods
    if os.path.getsize(AF_Prods) == 0 or not algunActivo():
        os.system("cls")
        print("Todavia no se cargo ningun producto")
        os.system("pause")
    else:
        os.system("cls")
        isInt = False
        cod = -1
        while cod != 0:
            while not isInt:
                cod = input("Ingrese el código del producto a modificar (0 para salir): ")
                isInt = verifInt(cod, 0, 99999)
            cod = int(cod)
            if cod != 0:
                pos = busqCod(cod, "B")
                if pos == -1:
                    print("El producto no está cargado")
                    os.system("pause")
                    os.system("cls")
                else:
                    AL_Prods.seek(pos)
                    reg = pickle.load(AL_Prods)
                    if not reg.cargado:
                        print("El producto no esta activo")
                        os.system("pause")
                    else:
                        print("Producto a modificar: ")
                        print("----------------------------")
                        print("| Código: " + '\t' + str(reg.cod))
                        print("| Nombre: " + '\t' + reg.nombre)
                        print("----------------------------")
                        print("Solo se puede modificar el nombre, de última dalo de baja")
                        reg.nombre = input("Ingrese el nuevo nombre: ").upper()
                        while len(reg.nombre) > 22 and len(reg.nombre) < 1:
                            print("Rta no aceptada, intente nuevamente")
                            os.system("pause")
                            os.system("cls")
                            reg.nombre = input("Ingrese el nuevo nombre: ").upper()
                        rta = input("Confirma? (Si/No): ").upper()
                        while rta != "SI" and rta != "NO":
                            rta = input("SI O NO?: ").upper()
                        if rta == "SI":
                            reg.nombre = reg.nombre.ljust(22)
                            AL_Prods.seek(pos)
                            pickle.dump(reg, AL_Prods)
                            AL_Prods.flush()
                isInt = False


def busqCamion(x):
    global AF_Ops, AL_Ops
    t = os.path.getsize(AF_Ops)
    AL_Ops.seek(0)
    while AL_Ops.tell() < t:
        pos = AL_Ops.tell()
        Ops = pickle.load(AL_Ops)
        if Ops.cod == x:
            return pos
    return -1


def checkTurnos(patente, fecha):
    global AF_Ops, AL_Ops
    t = os.path.getsize(AF_Ops)
    AL_Ops.seek(0)
    while AL_Ops.tell() < t:
        pos = AL_Ops.tell()
        Ops = pickle.load(AL_Ops)
        if Ops.patente == patente and Ops.fecha_cupo == fecha:
            return pos
    return -1


def entrega_cupos(cupos):
    print(cupos)
    os.system("cls")
    global AF_Prods, AF_Ops, AL_Ops
    if os.path.getsize(AF_Prods) == 0 or not algunActivo():
        print("Todavia no se cargo ningun producto, cargue uno y vuelva")
        os.system("pause")
        print(cupos)
        return cupos
    else:
        otro = True  # boolean
        while otro:
            otro = False
            new_patente = ""  # string
            while len(new_patente) < 6 or len(new_patente) > 7:
                new_patente = input("Ingrese la nueva patente: ")
                if len(new_patente) < 6 or len(new_patente) > 7:
                    print("Patente no aceptada")
                    os.system("pause")
            new_patente = new_patente.upper().ljust(7)
            ok = False
            while not ok:
                esFecha = False
                while not esFecha:
                    try:
                        fechaCupo = input("Ingrese la fecha del turno deseado (dd/mm/aaaa): ")
                        datetime.strptime(fechaCupo, "%d/%m/%Y")
                        esFecha = True
                    except:
                        print("Fecha invalida")
                        os.system("pause")
                f = fechaCupo.split('/')
                fechaCupo = f[2]+'-'+f[1]+'-'+f[0]
                if fechaCupo < str(date.today()):  # aaaa-mm-dd
                    print("El turno no puede ser para un dia anterior al actual")
                    os.system("pause")
                else:
                    ok = True
            if checkTurnos(new_patente, fechaCupo) != -1:
                print("La patente ya tiene cupo")
            else:
                isInt = False
                while not isInt:
                    cod = input("Ingrese el código del producto: ")
                    isInt = verifInt(cod, 1, 99999)
                cod = int(cod)
                pos = busqCod(cod, "B")
                if pos != -1:
                    if busqSilos(cod, "prod") != -1:
                        reg = Operacion()
                        reg.cod = str(cod).ljust(5)
                        reg.patente = new_patente.ljust(7)
                        reg.fecha_cupo = fechaCupo
                        reg.estado = 'P'
                        AL_Ops.seek(0, 2)
                        pickle.dump(reg, AL_Ops)
                        AL_Ops.flush()
                        rta = ""  # char
                        AL_Ops.seek(0)
                        reg = pickle.load(AL_Ops)
                        tReg = AL_Ops.tell()
                        cupos = os.path.getsize(AF_Ops) // tReg
                        while rta != "S" and rta != "N":
                            rta = input("Obtener otro cupo? S/N: ").upper()
                            if rta != "S" and rta != "N":
                                print("Rta no aceptada")
                                os.system("pause")
                        if rta == "S":
                            otro = True
                        else:
                            print(cupos)
                            return cupos
                    else:
                        print("No tenemos silos de ese producto. Volviendo al menú principal...")
                        os.system("pause")
                        print(cupos)
                        return cupos
                else:
                    print("No se ingresó un producto válido. Volviendo al menú principal...")
                    os.system("pause")
                    print(cupos)
                    return cupos
        print(cupos)
        return cupos


def menu_recepcion():  # camiones: array[7][1] de string[6]; estado:char
    os.system("cls")
    global AF_Ops, AL_Ops
    new_patente = ""  # string[6]
    if os.path.getsize(AF_Ops) == 0:
        print("Todavia no se otorgó ningun cupo")
        os.system("pause")
    else:
        while new_patente != "*":
            while (len(new_patente) < 6 or len(new_patente) > 7) and new_patente != "*":
                new_patente = input("Ingrese la patente (* para finalizar): ").upper()
                if (len(new_patente) < 6 or len(new_patente) > 7) and new_patente != "*":
                    print("Patente no aceptada")
                    os.system("pause")
            if new_patente != "*":
                new_patente = new_patente.ljust(7)
                ok = checkTurnos(new_patente, str(date.today()))
                if ok != -1:
                    AL_Ops.seek(ok)
                    reg = pickle.load(AL_Ops)

                    if reg.estado == 'P':
                        reg.estado = 'A'
                        AL_Ops.seek(ok)
                        pickle.dump(reg, AL_Ops)
                        AL_Ops.flush()
                elif ok == -1:
                    print("El camión no tiene turno para hoy")
                    os.system("pause")
                else:
                    print("El camión ya fue recibido o se encuentra en una etapa posterior")
                new_patente = ""


def ordenaRubros():
    global AL_Rubros, AF_Rubros
    AL_Rubros.seek(0)
    aux = pickle.load(AL_Rubros)
    tReg = AL_Rubros.tell()
    t = os.path.getsize(AF_Rubros)
    cantReg = t // tReg
    for i in range(0, cantReg-1):
        for j in range(i+1, cantReg):
            AL_Rubros.seek(i*tReg)
            auxi = pickle.load(AL_Rubros)
            AL_Rubros.seek(j*tReg)
            auxj = pickle.load(AL_Rubros)
            if auxi.cod > auxj.cod:
                AL_Rubros.seek(i*tReg)
                pickle.dump(auxj, AL_Rubros)
                AL_Rubros.seek(j*tReg)
                pickle.dump(auxi, AL_Rubros)


def busqDicRubro(x):
    global AL_Rubros, AF_Rubros
    x = int(x)
    AL_Rubros.seek(0)
    aux = pickle.load(AL_Rubros)
    tReg = AL_Rubros.tell()
    cantReg = os.path.getsize(AF_Rubros) // tReg
    min = 0
    max = cantReg - 1
    mid = (min + max) // 2
    AL_Rubros.seek(mid * tReg)
    rubro = pickle.load(AL_Rubros)
    while int(rubro.cod) != x and min < max:
        if x < int(rubro.cod):
            max = mid - 1
        else:
            min = mid + 1
        mid = (min + max) // 2
        AL_Rubros.seek(mid * tReg)
        rubro = pickle.load(AL_Rubros)
    if int(rubro.cod) == x:
        return mid*tReg
    else:
        return -1


def calidad():
    os.system("cls")
    global AL_Ops, AL_Prods, AL_Rubros, AF_Ops
    if os.path.getsize(AF_Ops) == 0:
        print("Todavia no se otorgó ningun cupo")
        os.system("pause")
    else:
        new_patente = ""
        while len(new_patente) < 6 or len(new_patente) > 7:
            new_patente = input("Ingrese la nueva patente: ")
            if len(new_patente) < 6 or len(new_patente) > 7:
                print("Patente no aceptada")
                os.system("pause")
                os.system("cls")
        new_patente = new_patente.upper().ljust(7)
        pos = checkTurnos(new_patente, str(date.today()))
        if pos != -1:
            AL_Ops.seek(pos)
            reg_ops = pickle.load(AL_Ops)
            codProd = int(reg_ops.cod)  # codigo del producto (en operaciones)
            if reg_ops.estado == 'A':
                posProd = busqCod(codProd, "B")
                AL_Prods.seek(posProd)
                reg = pickle.load(AL_Prods)  # Aca reg. es productos
                os.system("cls")
                print("----------------------------")
                print("| PRODUCTO: " + '\t' + reg.nombre)
                print("----------------------------")
                ordenaRubros()
                size = os.path.getsize(AF_RubroProds)
                AL_RubroProds.seek(0)
                strikes = 0
                while AL_RubroProds.tell() < size and strikes < 2:
                    reg = pickle.load(AL_RubroProds)  # aca reg es RxP
                    if int(reg.cod_prod) == codProd:
                        posRubro = busqDicRubro(reg.cod_rubro)
                        AL_Rubros.seek(posRubro)
                        rubro = pickle.load(AL_Rubros)
                        print("| Rubro: " + '\t' + rubro.nombre)
                        si = ""
                        while si != "SI":
                            isFloat = False
                            while not isFloat:
                                valor = input("| Ingrese el valor del rubro : ")
                                isFloat = verifFloat(valor, 0, 100)
                            si = input("| Revise y confirme (Si/No): ").upper()
                            while si != "SI" and si != "NO":
                                si = input("| Revise y confirme (Si/No): ").upper()
                        print("----------------------------")
                        if valor > reg.max or valor < reg.min:
                            strikes += 1
                if strikes < 2:
                    reg_ops.estado = 'C'
                    pickle.dump(reg_ops, AL_Ops)
                    AL_Ops.flush()
                    print(" Carga aprobada")
                    os.system("pause")
                else:
                    reg_ops.estado = 'R'
                    pickle.dump(reg_ops, AL_Ops)
                    AL_Ops.flush()
                    print(" Carga rechazada")
                    os.system("pause")
                print("----------------------------")
            else:
                print(" El camión se encuentra en otra etapa del proceso")
                os.system("pause")
        else:
            print(" La patente ingresada no tiene turno para hoy")
            os.system("pause")


def registro_pb():
    os.system("cls")
    global AL_Ops, AL_Prods, AF_Ops
    if os.path.getsize(AF_Ops) == 0:
        print(" Todavia no se otorgó ningun cupo")
        os.system("pause")
    else:
        new_patente = ""
        while len(new_patente) < 6 or len(new_patente) > 7:
            new_patente = input(" Ingrese la nueva patente: ")
            if len(new_patente) < 6 or len(new_patente) > 7:
                print(" Patente no aceptada")
                os.system("pause")
                os.system("cls")
        new_patente = new_patente.upper().ljust(7)
        pos = checkTurnos(new_patente, str(date.today()))
        if pos != -1:
            AL_Ops.seek(pos)
            reg_ops = pickle.load(AL_Ops)
            if reg_ops.estado == 'C':
                isInt = False
                while not isInt:
                    pb = input(" Ingrese el peso bruto (Máx 45tn): ")
                    isInt = verifInt(pb, 1, 45)
                pb = int(pb)
                pb = str(pb).ljust(2)
                reg_ops.bruto = pb
                reg_ops.estado = 'B'
                pickle.dump(reg_ops, AL_Ops)
                AL_Ops.flush()
                os.system("cls")
                os.system(" Peso bruto registrado")
                os.system("pause")
            else:
                print(" El camión se encuentra en otra etapa del proceso")
                os.system("pause")
        else:
            print(" La patente ingresada no tiene turno para hoy")
            os.system("pause")


def registro_tara():
    os.system("cls")
    global AF_Ops
    if os.path.getsize(AF_Ops) == 0:
        print(" Todavia no se otorgó ningun cupo")
        os.system("pause")
    else:
        new_patente = ""
        while len(new_patente) < 6 or len(new_patente) > 7:
            new_patente = input(" Ingrese la nueva patente: ")
            if len(new_patente) < 6 or len(new_patente) > 7:
                print(" Patente no aceptada")
                os.system("pause")
                os.system("cls")
        new_patente = new_patente.upper().ljust(7)
        pos = checkTurnos(new_patente, str(date.today()))
        if pos != -1:
            AL_Ops.seek(pos)
            reg_ops = pickle.load(AL_Ops)
            if reg_ops.estado == 'B':
                isInt = False
                while not isInt:
                    tara = input(" Ingrese la tara: ")
                    isInt = verifInt(tara, 1, int(reg_ops.bruto)-1)
                    if not isInt:
                        print(" La tara debe ser mayor al peso bruto")
                        os.system("pause")
                tara = int(tara)
                tara = str(tara).ljust(2)
                reg_ops.tara = tara
                reg_ops.estado = 'F'
                bt = int(reg_ops.bruto)
                pos = busqSilos(int(reg_ops.cod), "prod")
                pickle.dump(reg_ops, AL_Ops)
                AL_Ops.flush()
                AL_Silos.seek(pos)
                reg_silos = pickle.load(AL_Silos)
                reg_silos.stock += bt-int(tara)
                os.system("cls")
                os.system(" Tara registrada - Camión procesado por completo")
                os.system("pause")
            else:
                print("El camión se encuentra en otra etapa del proceso")
                os.system("pause")
        else:
            print("La patente ingresada no tiene turno para hoy")
            os.system("pause")


def reportes():
    os.system("cls")
    global AL_Silos, AF_Silos, AL_Prods
    global AF_Ops, AL_Ops, AL_Cupos

    AF_Promedios = "promedios.dat"
    AL_Promedios = open(AF_Promedios, "w+b")

    print("----------------------------")
    print("| REPORTES: ")
    print("----------------------------")
    AL_Cupos.seek(0)
    cupos = pickle.load(AL_Cupos)
    pickle.dump(cupos, AL_Cupos)
    print(cupos)
    print("| Cantidad de cupos otorgados:" + '\t' + str(cupos))
    print("----------------------------")

    t = os.path.getsize(AF_Ops)
    AL_Ops.seek(0)
    recibidos = 0
    while AL_Ops.tell() < t:
        Ops = pickle.load(AL_Ops)
        if Ops.estado != 'P':
            recibidos += 1
    print("| Cantidad de camiones recibidos:" + '\t' + str(recibidos))
    print("----------------------------")

    if os.path.getsize(AF_Silos) != 0:
        print("| Cantidad de camiones de...")
        recibidos = 0
        AL_Prods.seek(0)
        prom = Promedio()
        while AL_Prods.tell() < os.path.getsize(AF_Prods):
            prod = pickle.load(AL_Prods)
            AL_Ops.seek(0)
            while AL_Ops.tell() < t:
                Ops = pickle.load(AL_Ops)
                if Ops.cod == prod.cod and Ops.estado != 'P':
                    recibidos += 1
            prom.div = recibidos
            pickle.dump(prom, AL_Promedios)
            AL_Promedios.flush()
            print("| " + prod.nombre.strip() + '\t' + str(recibidos))

        print("----------------------------")
        print("| Peso total de cada producto: ")

        t = os.path.getsize(AF_Silos)
        AL_Silos.seek(0)
        AL_Promedios.seek(0)
        while AL_Silos.tell() < t:
            silo = pickle.load(AL_Silos)
            pos_prod = busqCod(int(silo.cod_prod), "B")
            AL_Prods.seek(pos_prod)
            prod = pickle.load(AL_Prods)
            prom.total = int(silo.stock)
            prom.nombre = prod.nombre
            print(prod.nombre.strip() + ":" + '\t' + str(silo.stock))
            pickle.dump(prom, AL_Promedios)
            AL_Promedios.flush()

        print("----------------------------")
        print("| Peso promedio por camión de...")
        AL_Promedios.seek(0)
        while AL_Promedios.tell() < os.path.getsize(AF_Promedios):
            prom = pickle.load(AL_Promedios)
            if prom.div != 0:
                print(prom.nombre.strip() + ':' + '\t' + str(prom.total/prom.div))
            else:
                print(prom.nombre.strip() + ':' + '\t' + "0.0")
        AL_Promedios.close()
        os.remove(AF_Promedios)

        print("----------------------------")
        print("| Camión de menor peso de...")
        AL_Prods.seek(0)
        min = 0
        patente_min = "-"
        while AL_Prods.tell() < os.path.getsize(AF_Prods):
            prod = pickle.load(AL_Prods)
            AL_Ops.seek(0)
            try:
                while AL_Ops.tell() < t:
                    Ops = pickle.load(AL_Ops)
                    if Ops.cod == prod.cod and (Ops.bruto-Ops.tara) < min:
                        min = Ops.bruto-Ops.tara
                        patente_min = Ops.patente.strip()
                print(prod.nombre.strip() + '\t' + patente_min)
            except:
                print(prod.nombre.strip() + '\t' + patente_min)
    os.system("pause")


def busq_Sec_1D(array, busq):
    i = 0
    N = len(array)
    while i < N and array[i] != busq:
        i += 1
    if i == N:
        return -1
    else:
        return i


def listadoSyR():
    os.system("cls")
    global AL_Silos, AF_Silos
    global AL_Ops, AF_Ops
    print("----------------------------")
    print("| Silo con mayor stock: ")
    silomax = "-"
    AL_Silos.seek(0)
    try:
        silo = pickle.load(AL_Silos)
        silomax = silo.nombre.strip()
        max = int(silo.stock)
        AL_Silos.seek(AL_Silos.tell())
        while AL_Silos.tell() < os.path.getsize(AF_Silos):
            silo = pickle.load(AL_Silos)
        print("| " + silomax)
    except:
        print("| " + silomax)

    esFecha = False
    while not esFecha:
        try:
            fecha = input("Ingrese la fecha del turno deseado (dd/mm/aaaa): ")
            datetime.strptime(fecha, "%d/%m/%Y")
            esFecha = True
        except:
            print("Fecha invalida")
            os.system("pause")
    f = fecha.split('/')
    print("| Patentes rechazadas: ")
    fecha = f[2] + '-' + f[1] + '-' + f[0]
    try:
        AL_Ops.seek(0)
        while AL_Ops.tell() < os.path.getsize(AF_Ops):
            reg = pickle.load(AL_Ops)
            if reg.estado == 'R':
                print("| "+reg.patente.strip)
    except:
        print("| -")
    os.system("pause")

#  programa main

archivos()

seleccion = "-"  # char
while seleccion != "0":
    menu_principal()
    seleccion = input("Seleccione una opcion: ")
    match seleccion:

        case "1":
            menu_administraciones()

        case "2":
            AL_Cupos.seek(0)
            cupos = pickle.load(AL_Cupos)
            print(cupos)
            cupos = entrega_cupos(cupos)
            print(cupos)
            pickle.dump(cupos, AL_Cupos)
            AL_Cupos.flush()

        case "3":
            menu_recepcion()

        case "4":
            calidad()

        case "5":
            registro_pb()

        case "6":
            print("Proceso en construcción\n")
            os.system("pause")

        case "7":
            registro_tara()

        case "8":
            reportes()

        case "9":
            listadoSyR()

        case "0":
            print("FIN DEL PROGRAMA")
            AL_RubroProds.close()
            AL_Silos.close()
            AL_Rubros.close()
            AL_Prods.close()
            AL_Ops.close()
            AL_Cupos.close()

        case other:
            print("Opcion incorrecta, seleccione otra")
            os.system("pause")
