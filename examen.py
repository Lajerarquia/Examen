#CSV
from os import system
system("cls")
import re

#Las Listas
trabajadores = []
sueldos3k = []
sueldos2m3k = []
sueldos2m = []
total_sueldos = []
nombre = []
apellido = []
contador_sueldos = []
rut = ['20.932.990-5']
desarrollador = ['Benjamín Palma']
promedio_sueldos = []
descuento_salud = []
descuento_afp = []
sueldo_liquido = []
contador_sueldos3k = []
contador_sueldos2m3k = []
contador_sueldos2m = []
sueldos = []

#Def Validaciones
def validar_numero(sueldos3k):
    return sueldos3k.isdigit() and int(sueldos3k) > 0

def validar_numero(sueldos2m3k):
    return sueldos2m3k.isdigit() and int(sueldos2m3k) > 0

def validar_numero(sueldos2m):
    return sueldos2m.isdigit() and int(sueldos2m) > 0

def validar_minimo(sueldos3k):
    return re.match(r'^\d{1,800000}$', sueldos3k)

def validar_minimo(sueldos2m3k):
    return re.match(r'^\d{800000,1999999}$', sueldos2m3k)

def validar_minimo(sueldos2m):
    return re.match(r'^\d{1999999,25000000}$', sueldos2m)

#Def Objetos
def menu():
    print("1.   Asignar Sueldos Aleatorios")
    print("2.	Clasificar Sueldos")
    print("3.	Ver Estadísticas")
    print("4.	Reporte De Sueldos")
    print("5.	Salir Del Programa")

#Menu
menu()
opcion=input("\nIngrese una opción: ")
#Asignar Sueldos Aleatorios
if opcion=="1":
        def registrar_consumo():
            nombre=input("Ingrese Nombre: ")
            apellido=input("Ingrese Apellido: ")
            sueldo3k=input("Ingrese Sueldo si es que es menor a $800.000: ")
            if sueldo3k == 0:
                print("el sueldo ingresado no es menor a 800.000")
            elif sueldo3k <= 0:
                contador_sueldos3k = contador_sueldos3k = contador_sueldos3k + 1
            sueldo2m3k=input("Ingrese Sueldo si es que es entre $800.000 y $2.500.000: ")
            if sueldo2m3k == 0:
                print("el sueldo ingresado no esta entre 800.000 y 2.000.000")
            elif sueldo2m3k <= 0:
                contador_sueldos2m3k = contador_sueldos2m3k = contador_sueldos2m3k + 1
            sueldo2m=input("Ingrese Sueldo si es que es superior a $2.000.000: ")
            if sueldo2m == 0:
                print("el sueldo ingresado no es mayor a 2.000.000")
            elif sueldo2m <= 0:
                contador_sueldos2m = contador_sueldos2m = contador_sueldos2m + 1
            sueldos = {
            "nombre":nombre,
            "apellido":apellido,
            "sueldo menor a 800.000":sueldo3k,
            "sueldo entre 800.000 y 2.000.000":sueldo2m3k,
            "sueldo superior 2.000.000":sueldo2m,
            }
            total_sueldos.append(sueldos)
            total_sueldos.append(contador_sueldos)
            menu()
#Mostar Sueldos 'Menores a 800k$, Entre 800k$ y 2M$, Superior a 2M$, Total Sueldos'
elif opcion=="2":
        print("sueldos menores a $800.000")
        print(f"total: {contador_sueldos3k}")
        for i in range(len(sueldos3k)):
            print(f"[{i + 1}] {sueldos3k[i]}")
        print("sueldos entre $800.000 y $2.000.000")
        print(f"total: {contador_sueldos2m3k}")
        for i in range(len(sueldos2m3k)):
            print(f"[{i + 1}] {sueldos2m3k[i]}")
        print("sueldos mayores $2.000.000")
        print(f"total: {contador_sueldos2m}")
        for i in range(len(sueldos2m)):
            print(f"[{i + 1}] {sueldos2m[i]}")
        print("nombres")
        for i in range(len(nombre)):
            print(f"[{i + 1}] {nombre[i]}")
        print("apellidos")
        for i in range(len(apellido)):
            print(f"[{i + 1}] {apellido[i]}")
        print(f"total sueldos: ${total_sueldos}")
        menu()
#Ver Estadisticas 'Sueldo más alto, Sueldo más bajo, Promedio de Sueldos, Media Geométrica'
elif opcion=="3":
    promedio_sueldos = total_sueldos % contador_sueldos
    print("-------------------------------")
    print("          E S T A D I S T I C A        ")
    print("-------------------------------")
    print(f"sueldo más alto:            {sueldos2m.sueldo_más_alto}")
    print(f"sueldo más bajo:         {sueldos3k.sueldo_más_bajo}")
    print(f"promedio de sueldos:       {promedio_sueldos.promedio_de_sueldos}")
    print(f"media geométrica:       {geometric_mean(total_sueldos).media_geométrica}")
    print("-------------------------------")
    menu()
#Detalle de Sueldos 'Descuento Salud 7%, Descuento AFP 12%, Sueldo Liquido'
elif opcion=="4":
    descuento_salud = total_sueldos * 0.07
    descuento_salud = descuento_salud - total_sueldos
    descuento_afp = total_sueldos * 0.12
    descuento_afp = descuento_afp - total_sueldos
    sueldo_liquido = descuento_salud + descuento_salud - total_sueldos
    print("-------------------------------")
    print("          R E P O R T E                  ")
    print("-------------------------------")
    print(f"descuento salud 7% :            {descuento_salud.descuento_salud}")
    print(f"descuento afp 12%:         {descuento_afp.descuento_afp}")
    print(f"sueldo liquido:       {sueldo_liquido.sueldo_liquido}")
    print("-------------------------------")
#exportar a archivo csv
    archivo_re="reporte.csv"
    with open(archivo_re, "W") as archivo:
        for total_sueldos in opcion=="4":
            destino_re=f"{descuento_salud.descuento_salud, descuento_afp.descuento_afp, sueldo_liquido.sueldo_liquido} "
            archivo.write("'descuento salud'\t\t'descuento afp'\t\t'sueldo liquido'")
            archivo.write(destino_re)
            input("Archivo creado")
    menu()
#Cerrar Progama 'Nombre y Rut del Progamador'
elif opcion=="4":
    print(f"rut = {rut.rut}")
    print(f"desarrollado por= {desarrollador.desarrollador}")
    menu()