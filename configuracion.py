from functions_number.generator import generar_0_a_10, generar_0_a_100, generar_0_a_1000
from jugarFinaly import jugar

def elegir_amplitud_y_intentos():
    # Mostrar las opciones de amplitud y número de intentos
    print("\n\033[1;33m--- CONFIGURACIÓN DEL JUEGO ---\033[0m")
    
    # Opciones de amplitud
    print("\033[1;34m--- Elige la amplitud del número ---\033[0m")
    print("1. Números de 0 a 10")
    print("2. Números de 0 a 100")
    print("3. Números de 0 a 1000")
    
    amplitud = input("Elige una opción de amplitud: ")
    numero_secreto = None

    if amplitud == "1":
        numero_secreto = generar_0_a_10()
        print("\n\033[1;33m--- Has elegido números de 0 a 10 ---\033[0m")
    elif amplitud == "2":
        numero_secreto = generar_0_a_100()
        print("\n\033[1;33m--- Has elegido números de 0 a 100 ---\033[0m")
    elif amplitud == "3":
        numero_secreto = generar_0_a_1000()
        print("\n\033[1;33m--- Has elegido números de 0 a 1000 ---\033[0m")
    else:
        print("\n\033[1;31m--- Opción no válida ---\033[0m")
        return None, None, None

    # Opciones de intentos
    print("\033[1;34m--- Elige el número de intentos ---\033[0m")
    print("1. 3 intentos")
    print("2. 4 intentos")
    print("3. 5 intentos")
    print("4. 6 intentos")
    print("5. 7 intentos")

    intentos = input("Elige una opción de intentos: ")
    if intentos == "1":
        intentos = 3
        print("\n\033[1;33m--- Has elegido 3 intentos ---\033[0m")
    elif intentos == "2":
        intentos = 4
        print("\n\033[1;33m--- Has elegido 4 intentos ---\033[0m")
    elif intentos == "3":
        intentos = 5
        print("\n\033[1;33m--- Has elegido 5 intentos ---\033[0m")
    elif intentos == "4":
        intentos = 6
        print("\n\033[1;33m--- Has elegido 6 intentos ---\033[0m")
    elif intentos == "5":
        intentos = 7
        print("\n\033[1;33m--- Has elegido 7 intentos ---\033[0m")
    else:
        print("\n\033[1;31m--- Opción no válida ---\033[0m")
        return None, None, None

    # Pasar los datos a la función jugar
    jugar(numero_secreto, intentos)
    return numero_secreto, amplitud, intentos
