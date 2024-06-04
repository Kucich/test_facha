# Cartelito

#Consignas:
#Que con solo una ejecución pueda realizar mas de un cartel, 
#haciendo que solo tipeo de ENTER termine el programa.
#Que el cartel sea siempre mostrado en MAYÚSCULAS.
#Que los espacios a la derecha e izquierda del texto ingresado sean ignorados.
#Que la pantalla de la terminal sea borrada antes de solicitar el ingreso de texto.
#Que luego de mostrar el cartel aparezca el texto 
#"Pulse <Enter> para retornar." y que esa acción lleve al operador 
#a ingresar un nuevo texto.
#Que los carácteres + - | sean reemplazados por caracteres unicode 
#que permitan dibujar bordes completos, simples o dobles, 
#lo dejo a criterio de c/u.

import atexit
import os

def limpiar_terminal():
    os.system('clear')  # Esto limpia la pantalla de la terminal

# Registra la función para ser llamada al finalizar el programa
atexit.register(limpiar_terminal)

while True:
    cartel = input("Introduzca texto o pulse ENTER para salir: ").upper().strip()

    while cartel != "":

        if len(cartel):
            print("+---" * len(cartel) + "+")

        for i in cartel:
            print("| " + i + " ", end='')

        if len(cartel): 
            print("|")

        if len(cartel):
            print("+---" * len(cartel) + "+")
        
        cartel = input("Escriba RETORNAR para volver: ").upper().strip()

        if "RETORNAR" == cartel:
            break
        else:
            while cartel != "RETORNAR":
                cartel = input("Porfavor ingrese RETORNAR: ").upper().strip()

                if "RETORNAR" == cartel:
                    break
        
        if "RETORNAR" == cartel:
            break

    if not cartel:
            break