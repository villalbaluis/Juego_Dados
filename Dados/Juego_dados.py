import os
import random as r
from colorama import *
import json

# La libreria JSON solo la usamos para la impresión de los jugadores 

# Colorama se usa para dar colores a los mensajes que se muestran en consola
# mediante los Fore."algunColor" se pinta el mensaje

os.system('cls')

# Lista que contendra diccionarios donde se tienen todos los jugadores con sus datos
datos_jugadores = []

# Esta función recibe como parametro una lista, la cual se validan ciertas posicicones para asignar al diccionario del jugador
def validar_valores(lista_valores):
    # En valor_dados_jugador guardamos en un solo valor, todos los resultados de los dados que vienen en la lista_valores
    valor_dados_jugador = lista_valores[1], lista_valores[2],  lista_valores[3],  lista_valores[4],  lista_valores[5]
    # Creamos el diccionario donde se guarda la información del jugador
    jugador = {
            # lista_valores[0] hace referencia al nombre del jugador en la lista entrante, recibida en la fución
            "Nombre": lista_valores[0], 
            "Dado": valor_dados_jugador,
            # para todos los jugadores, la apuesta inicial será de 500 pesos
            "Apuesta": 500
        }
    
    # Vamos a guardar el diccionario de la información del jugador, en la lista de todos los jugadores (datos_jugadores)
    # Primero validamos si tiene datos esa lista a travéz de len(datos_jugadores)
    # si devuelve un 0 es porque no hay jugadores registrados, y registramos el primero de ellos
    if(len(datos_jugadores) == 0):
        datos_jugadores.append(jugador)
        # Luego de registrar el dict del jugador a la list datos_jugadores con la función append
        # Volvemos a tirar los dados para el siguiente turno
        tirar_dados()
    # Pero si la lista de datos_jugadores si tiene datos, validamos los dados tirados
    elif(len(datos_jugadores) >= 1):
        # Validamos primero si alguno de los dados que lanzo dió como valor 1, esto validando la lista de entrada de los datos
        if(1 not in lista_valores):
            # Si no hay un 1 en esa lista, mostramos que pierde el turno...
            print(Fore.RED + Style.BRIGHT + lista_valores[0] + ", no has tenido suerte, por favor, cede tu turno." + Style.RESET_ALL)
            # Y a ese jugador en especifico se le deben sumar otros 500 al monto de la apuesta
            for dato in datos_jugadores:
                # Este tipo de foreach, busca comparar mostrar validar, lo que se necesite de un solo jugador
                # cada (dato) de los datos_jugadores es un jugador individual con su información
                if(lista_valores[0] ==  dato["Nombre"]):
                    # Si encuentra al jugador, aunmentará la apuesta en 500 pesos
                    dato["Apuesta"] = dato["Apuesta"] + 500
                    break
                # Rompemos el ciclo de busqueda de ese especifico jugador, y pasamos a lanzar los dados de nuevo
            os.system('pause')
            tirar_dados()
        else:
            # Pero si encontramos que alguno de los dados ha dado el valor 1, debemos actualizar la info del jugador
            for dato in datos_jugadores:
                if(lista_valores[0] ==  dato["Nombre"]):
                    # Buscamos al jugador por el nombre en la lista de jugadores, si lo encontramos 
                    # ponemos en el valor de los dados del jugador los nuevos resultados de los dados, 
                    # reemplazando los anteriors
                    dato["Dado"] = valor_dados_jugador
                    break
                # Igual, rompemos ese ciclo de busqueda, y pasamos a mirar cuantos 1 sacarón
        # Contamos cuantos 1 tiene esa lista_valores, e imprimimos que parte de la cucaracha se formó para luego volver a tirar los datos
        contar_unos = lista_valores.count(1)
        if(contar_unos == 1):
            print("Lograste formar las costillas")
        elif(contar_unos == 2):
            print("Lograste formar la cabeza")
        elif(contar_unos >= 3):
            print("Lograste formar la cola")
        elif(contar_unos >= 5):
            print(Fore.LIGHTGREEN_EX + "¡Felicidades! Has formado toda la cucaracha")
        os.system('pause')
        tirar_dados()

def tirar_dados():
    os.system('cls')
    # Esta lista llevará los datos del juego actual, donde se tendrá nombre del jugador, y valores de los dados
    # tendrá un formato de este estilo: ["Luis", "1","2","3","4","5"]
    # donde cada numero hace referencia a cada valor de cada dado obtenido
    valores_dados = []
    # con el .clear, aseguramos que la lista este vacia antes de empezar el juego, así no se repetirán datos
    valores_dados.clear()
    # Le decimos al usuario que quiere hacer, si un nuevo juego, o ver los datos de jugadores
    print(Fore.GREEN + "Hola jugador, ¿Cuál es tu nombre?: " + Fore.YELLOW + "(Ingrese número '1' para ver los datos guardados) " + Style.RESET_ALL)
    nombre_jugador = str(input().lower())
    # Si quiere ver datos de jugadores será el 1 que ingrese por teclado, 
    # donde lo enviar a la función mostrar_datos()
    if(nombre_jugador == "1"):
        apostadores = mostrar_datos()
    # si ingresa cualquier otro valor, se iniciara el juego, y guardamos el nombre del jugador en la lista
    else:
        valores_dados.append(nombre_jugador)

    # Para cada dado es igual, se crea la variable del dato, se asigna el random del 1 al 6
    # y se agrega el resultado a la lista con todos los datos_jugadores
    dado_uno = r.randint(1,6)
    valores_dados.append(dado_uno)

    dado_dos = r.randint(1,6)
    valores_dados.append(dado_dos)

    dado_tres = r.randint(1,6)
    valores_dados.append(dado_tres)

    dado_cuatro = r.randint(1,6)
    valores_dados.append(dado_cuatro)

    dado_cinco = r.randint(1,6)
    valores_dados.append(dado_cinco)
    
    # Aquí obtenenmos todos los dados, solo para mostralos graficamente en el mensaje de abajo
    dados_obtenidos = dado_uno, dado_dos, dado_tres, dado_cuatro, dado_cinco
    print('╔════════════════════════════════════════════════╗')
    print('║' + Fore.MAGENTA + '    Tu suerte ha hablado, tus dados dieron'  + Style.RESET_ALL + '      ║')
    print('║            ' , dados_obtenidos ,'                   ║')
    print('╚════════════════════════════════════════════════╝')
    os.system('pause')
    # Indicamos el inicio de la validación de los valores, pasando la lista con los datos recopilados
    validar_valores(valores_dados)
    return valores_dados

# Con esta función mostraremos los datos de los jugadores en la partida
def mostrar_datos():
    os.system('cls')
    # Validamos primero si tenemos datos registrados, de no ser así, mostramos el mensaje
    if(len(datos_jugadores) == 0):
        print(Fore.RED + "No tenemos registros para mostrar")
    # Pero si hay datos registrados, vamos diccionario por diccionario de cada jugador
    elif(len(datos_jugadores) >= 1):
        # Cada dato es un jugador de la lista con diccionarios llamado datos_jugadores
        for dato in datos_jugadores:
            # Al querer imprimir solo uno por uno tenemos dos opciones 
            # Imprimir en un formato tipo JSON
            print(json.dumps(dato, indent=2))
            # O en una tipo de cajita
            for k, v in dato.items():
                print('╔════════════════════════╗')
                print('║' , k , '║' , v , '         ║')
                print('╚════════════════════════╝')
    os.system('pause')
    tirar_dados()
    
# Todo el programa se inicializa desde aquí, haciendo el llamado por primera vez para la función de lanzar dados
dado = tirar_dados()

def imprimir_dado(valor):
    if (1 in valor):
        print('╔═══════╗')
        print('║       ║')
        print('║   1   ║')
        print('║       ║')
        print('╚═══════╝')
    else:
        if (2 in valor):
            print('╔═══════╗')
            print('║2      ║')
            print('║       ║')
            print('║      2║')
            print('╚═══════╝')
        else:
            if (3 in valor):
                print('╔═══════╗')
                print('║3      ║')
                print('║   3   ║')
                print('║      3║')
                print('╚═══════╝')
            else:
                if (4 in valor):
                    print('╔═══════╗')
                    print('║4     4║')
                    print('║       ║')
                    print('║4     4║')
                    print('╚═══════╝')
                else:
                    if (5 in valor):
                        print('╔═══════╗')
                        print('║5     5║')
                        print('║   5   ║')
                        print('║5     5║')
                        print('╚═══════╝')
                    else:
                        if (6 in valor):
                            print('╔═══════╗')
                            print('║6     6║')
                            print('║6     6║')
                            print('║6     6║')
                            print('╚═══════╝')