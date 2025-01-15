# Variables globales para almacenar los números generados
numero_0_10 = None
def generar_0_a_10():
    global numero_0_10
    numero_0_10 = (7 * 3 + 4) % 11  # Ejemplo de fórmula para generar un número de 0 a 10
    return numero_0_10

# Variables globales para almacenar los números generados
numero_0_100 = None
def generar_0_a_100():
    global numero_0_100
    numero_0_100 = (15 * 7 + 8) % 101  # Ejemplo de fórmula para generar un número de 0 a 100
    return numero_0_100

# Variables globales para almacenar los números generados
numero_0_1000 = None
def generar_0_a_1000():
    global numero_0_1000
    numero_0_1000 = (21 * 13 + 5) % 1001  # Ejemplo de fórmula para generar un número de 0 a 1000
    return numero_0_1000