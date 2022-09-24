import os
import random as r
from colorama import *
import json


def lanzar_dados():
    os.system('cls')

    judadores = { }
    fr = (Fore.GREEN + "Hola jugador, mide tu suerte, ¿Cuál es tu nombre? : " + Style.RESET_ALL)
    nombre_jugador = input(fr).lower()
    
    #    Creas un nuevo diccionario para guardar los nuevos valores
    jugador = {
        'Apuesta': 0,
        'Dados': []
    }

    jugador['Apuesta'] = input(f'Cuánto apuestas?:   ')

    #    Lanza los dados
    for i in range(6):
        input(f'{nombre_jugador.title()} pulsa enter para tirar el dado {i+1}')
        jugador['Dados'].append(r.randint(1,3))

    #   Cuenta los 1
    print(f"{nombre_jugador} tienes {jugador['Dados'].count(1)}")

    #   Guarda los datos en el dicc jugadores

    judadores[nombre_jugador] = jugador
    
juego = lanzar_dados()