# Bonaroti, Francisco 111
# Cosenza, Teo 107
# Gilardoni, Lucio 107
# Vacs, Francisco 107

import os
import os.path
import pickle
import io
from datetime import datetime
from datetime import date
from turtle import pos


class Operacion:
    def __init__(self):
        self.patente = ""
        self.cod_prod = 0
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


global AL_RubroProds, AF_RubroProds
global AL_Silos, AF_Silos
global AL_Rubros, AF_Rubros
global AL_Prods, AF_Prods
global AL_Ops, AF_Ops


def archivos():
    global AL_RubroProds, AF_RubroProds
    global AL_Silos, AF_Silos
    global AL_Rubros, AF_Rubros
    global AL_Prods, AF_Prods
    global AL_Ops, AF_Ops
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
        print("El codigo de producto debe ser un numero entero")
        return False


def busqCod(cod, x):
    global AL_RubroProds, AF_RubroProds
    global AL_Silos, AF_Silos
    global AL_Rubros, AF_Rubros
    global AL_Prods, AF_Prods
    match x:
        case "B":
            AF_Aux = AF_Prods
            AL_Aux = AL_Prods
        case "C":
            AF_Aux = AF_Rubros
            AL_Aux = AL_Rubros
        case "E":
            AF_Aux = AF_Silos
            AL_Aux = AL_Silos
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
            if pos != -1:
                reg.cod_rubro = str(cod).ljust(5)
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
                pos = busqCod(cod, "E")
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
                            reg.cod_prod = str(codP).ljust(5)
                        else:  # Refinar busqCod para q no incluya inactivos (agregar otra f(x))
                            print("El código ingresado no corresponde con ningún producto cargado")
                    pickle.dump(reg, AL_Silos)
                    AL_Silos.flush()
                else:
                    print("Silo ya ingresado")
                    os.system("pause")
                isInt = False


def altaRxP():
    global AL_RubroProds, AF_RubroProds
    global AF_Rubros, AF_Prods
    if os.path.getsize(AF_Rubros) == 0 or os.path.getsize(AF_Prods) or not algunActivo():  # tmb ver si estan todos dados de baja
        os.system("cls")
        print("Todavía no se cargó ningún rubro y/o producto")
        os.system("pause")
    isInt = False
    cod = -1
    reg = Rubro_prod()
    while not isInt:
        codR = input("Ingrese el código del rubro: ")
        isInt = verifInt(codR, 1, 99999)
    isInt = False
    codR = str(codR).ljust(5)
    pos = busqCod(codR, "C")
    if pos != -1:
        while not isInt:
            codP = input("Ingrese el código del producto: ")
            isInt = verifInt(codP, 1, 99999)
        codP = str(codP).ljust(5)
        pos = busqCod(codP, "C")
        AL_Prods.seek(pos)
        reg = pickle.load(AL_Prods)
        if pos != -1 and reg.cargado:
            reg.cod_rubro = codR
            reg.cod_prod = codP
            isFloat = False
            while not isFloat:
                min = input("Ingrese el valor mínimo: ")
                isFloat = verifFloat(min, 0, 100)
            isFloat = False
            reg.min = str(min).ljust(8)
            while not isFloat:
                max = input("Ingrese el valor máximo: ")
                isFloat = verifFloat(max, min, 100)
            reg.max = str(max).ljust(8)
            pickle.dump(reg, AL_RubroProds)
            AL_RubroProds.flush()
        else:
            print("Producto no ingresado")
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
        print("El codigo de producto debe ser un numero real")
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
        Ops = pickle.load(AL_Ops)
        if Ops.patente == patente and Ops.fecha_cupo == fecha:
            return pos
    return -1


def entrega_cupos():
    os.system("cls")
    global AF_Prods, AF_Ops, AL_Ops
    if os.path.getsize(AF_Prods) == 0 or not algunActivo():
        print("Todavia no se cargo ningun producto, cargue uno y vuelva")
        os.system("pause")
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
                new_patente = new_patente.upper()
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
            if checkTurnos(new_patente,fechaCupo) != -1:
                print("La patente ya tiene cupo")
            else:
                isInt = False
                while not isInt:
                    cod = input("Ingrese el código del producto: ")
                    isInt = verifInt(cod, 1, 99999)
                    cod = int(cod)
                pos = busqCod(cod, "B")
                print(pos)
                if pos != -1:
                    reg = Operacion()
                    reg.cod_prod = str(cod).ljust(5)
                    reg.patente = new_patente.ljust(7)
                    reg.fecha_cupo = fechaCupo
                    reg.estado = 'P'
                    AL_Ops.seek(0, 2)
                    pickle.dump(reg, AL_Ops)
                    AL_Ops.flush()
                    rta = ""  # char
                    while rta != "S" and rta != "N":
                        rta = input("Obtener otro cupo? S/N: ").upper()
                        if rta != "S" and rta != "N":
                            print("Rta no aceptada")
                            os.system("pause")
                    if rta == "S":
                        otro = True
                    else:
                        return pos+1
                else:
                    print("No se ingresó un producto válido. Volviendo al menú principal...")
                    os.system("pause")
                    return pos
                return pos
        

def menu_recepcion(camiones, estado):  # camiones: array[7][1] de string[6]; estado:char
    os.system("cls")
    global AF_Prods, AF_Ops, AL_Ops
    new_patente = ""  # string[6]
    if os.path.getsize(AF_Ops) == 0:
        print("Todavia no se entrego ningún cupo")
    else:
        while new_patente != "*":
            while (len(new_patente) < 6 or len(new_patente) > 7) and new_patente != "*":
                new_patente = input("Ingrese la nueva patente (* para finalizar): ").upper()
                if (len(new_patente) < 6 or len(new_patente) > 7) and new_patente != "*":
                    print("Patente no aceptada")
                    os.system("pause")
            if new_patente != "*":
                ok = checkTurnos(new_patente,str(date.today()))
                AL_Ops.seek(pos)
                reg = pickle.load(AL_Ops)
                AL_Ops.seek(pos)
                if ok != -1 and reg.estado == 'P':
                    reg.estado = 'A'
                    pickle.dump(reg, AL_Ops)
                    AL_Ops.flush()
                elif ok != -1:
                    print("El camión no tiene turno para hoy")
                    os.system("pause")
                else:
                    print("El camión ya fue recibido o se encuentra en una etapa posterior")


def ordenaRubros():
    global AL_Rubros, AF_Rubros
    AL_Rubros.seek(0)
    aux = pickle.load(AL_Rubros)
    tReg = AL_Rubros
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

def calidad():
    ordenaRubros()

def registro_pb(camiones, estado,
                pesos):  # camiones: array[7][1] de string[6]; estado:array[7] de char; pesos: array[2] de int
    os.system("cls")
    """if camiones[0][0] != "":
        patente = ""  # string[6]
        while len(patente) < 6 or len(patente) > 7:
            patente = input("Ingrese la patente del camion: ").upper()
            if len(patente) < 6 or len(patente) > 7:
                print("Patente no aceptada")
                os.system("pause")
        i = 0  # int
        while i < 8 and patente != camiones[i][0]:
            i += 1
        if i < 8 and pesos[i][0] == 0:
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
        os.system("pause")"""


def registro_tara(camiones, estado,
                  pesos):  # camiones: array[7][1] de string[6]; estado:array[7] de char; pesos: array[2] de int
    os.system("cls")
    if camiones[0][0] != "":
        patente = ""  # string[6]
        while len(patente) < 6 or len(patente) > 7:
            patente = input("Ingrese la patente del camion: ").upper()
            if len(patente) < 6 or len(patente) > 7:
                print("Patente no aceptada")
                os.system("pause")
        i = 0  # int
        while i < 8 and patente != camiones[i][0]:
            i += 1
        if i < 8 and pesos[i][1] == 0:
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
            print("La tara de este camion ya fue registrada")
            os.system("pause")
    else:
        print("Todavia no se asigno ningun cupo")
        os.system("pause")


def reportes(cupos, estado, camiones, pesos,
             cargados):  # cupos: int; estado:array[7] de char; camiones:array[7][1] de string[6]; pesos: array[2] de int; cargados: array[2] de string[6]
    os.system("cls")
    print("Se entregaron " + str(cupos) + " cupos")
    i = 0  # int
    recibidos = 0  # int
    camiones_prod = [0] * 3  # array[2] de string[7]
    pesos_netos = [0] * 3  # array[2] de int

    while i < 8:
        if estado[i] == 'E' or estado[i] == 'C':
            recibidos += 1
        if camiones[i][0] != "":
            for j in range(2):
                if camiones[i][1] == cargados[j]:
                    camiones_prod[j] += 1
                    pesos_netos[j] += pesos[i][2]
        i += 1

    print("Se recibieron " + str(recibidos) + " camiones")

    if recibidos > 1:
        for i in range(3):
            if cargados[i] != "":
                if camiones_prod[i] > 0:
                    print("Hay " + str(camiones_prod[i]) + " camiones de " + cargados[i])
                    print("Peso neto promedio de " + cargados[i] + ": " + str(pesos_netos[i] / camiones_prod[i]))
                    j = 0  # int
                    neto_max = 0  # int
                    patente_max = ""  # string[6]
                    while j < 8:
                        if camiones[j][1] == cargados[i] and neto_max <= pesos[j][2]:
                            neto_max = pesos[j][2]
                            patente_max = camiones[j][0]
                        j += 1
                    print("Patente que más " + cargados[i] + " trajo: " + patente_max)
                    j = 0
                    neto_min = neto_max  # int
                    patente_min = patente_max  # string[6]
                    while j < 8:
                        if camiones[j][1] == cargados[i] and neto_min >= pesos[j][2]:
                            neto_min = pesos[j][2]
                            patente_min = camiones[j][0]
                        j += 1
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


def busq_Sec_1D(array, busq):
    i = 0
    N = len(array)
    while i < N and array[i] != busq:
        i += 1
    if i == N:
        return -1
    else:
        return i


# programa main

archivos()

cargados = [""] * 3  # array[2] de string[6]
camiones = [""] * 8  # array[7][2] de string[6]
for i in range(8):
    camiones[i] = [""] * 2
estado = ["-"] * 8  # array[7] de char
pesos = [0] * 8  # array[7][2] de int
for i in range(8):
    pesos[i] = [0] * 3
cupos = 0  # int

seleccion = "-"  # char
while seleccion != "0":
    menu_principal()
    seleccion = input("Seleccione una opcion: ")

    if seleccion == "1":
        menu_administraciones()

    elif seleccion == "2":
        cupos = entrega_cupos(camiones, estado, cargados[:])

    elif seleccion == "4":
        calidad()
    elif seleccion == "9":
        print()

    elif seleccion == "6":
        print("Proceso en construcción\n")
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
        AL_RubroProds.close()
        AL_Silos.close()
        AL_Rubros.close()
        AL_Prods.close()
        AL_Ops.close()

    else:
        print("Opcion incorrecta, seleccione otra")
        os.system("pause")
