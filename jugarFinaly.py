
def jugar(numero_secreto, intentos):
    print(f"\n\033[1;32m--- ¡Comencemos a jugar! ---\033[0m")
    print(f"Tienes {intentos} intentos para adivinar un número.")

    for intento in range(1, intentos + 1):
        try:
            guess = int(input(f"Intento {intento}: Ingresa tu número: "))
        except ValueError:
            print("\033[1;31m--- Entrada no válida, intenta de nuevo. ---\033[0m")
            continue

        if guess == numero_secreto:
            print("\033[1;32m--- ¡Felicidades! Has adivinado el número secreto. ---\033[0m")
            break
        elif guess < numero_secreto:
            print("\033[1;33m--- Demasiado bajo. Intenta de nuevo. ---\033[0m")
        else:
            print("\033[1;33m--- Demasiado alto. Intenta de nuevo. ---\033[0m")
    else:
        print(f"\033[1;31m--- Lo siento, has agotado tus intentos. El número secreto era {numero_secreto}. ---\033[0m")
