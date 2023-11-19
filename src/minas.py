"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random #Herramienta que nos proporciona herramientas para generar numeros aleatorios

def imprimir_tablero(tablero_visible):
    for fila in tablero_visible:
        print(" ".join(fila))
    print()

def colocar_minas(filas, columnas, num_minas):
    minas = set()
    while len(minas) < num_minas:
        mina = (random.randint(0, filas - 1), random.randint(0, columnas - 1))
        minas.add(mina)
    return minas

def contar_minas_alrededor(tablero, fila, columna):
    filas, columnas = len(tablero), len(tablero[0])
    direcciones = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    contador = 0

    for d_fila, d_columna in direcciones:
        nueva_fila, nueva_columna = fila + d_fila, columna + d_columna
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and tablero[nueva_fila][nueva_columna] == 'X':
            contador += 1

    return contador

def crear_tablero(filas, columnas, minas):
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    for fila, columna in minas:
        tablero[fila][columna] = 'X'

    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] != 'X':
                minas_alrededor = contar_minas_alrededor(tablero, fila, columna)
                tablero[fila][columna] = str(minas_alrededor) if minas_alrededor > 0 else ' '

    return tablero

def inicializar_tablero(filas, columnas, num_minas):
    minas = colocar_minas(filas, columnas, num_minas)
    tablero_real = crear_tablero(filas, columnas, minas)
    tablero_visible = [[' ' for _ in range(columnas)] for _ in range(filas)]
    celdas_destapadas = set()
    return tablero_real, tablero_visible, celdas_destapadas, minas

def revelar_celda(tablero_visible, tablero_real, fila, columna, celdas_destapadas):
    if (fila, columna) not in celdas_destapadas:
        celdas_destapadas.add((fila, columna))
        tablero_visible[fila][columna] = tablero_real[fila][columna]

        if tablero_real[fila][columna] == ' ':
            filas, columnas = len(tablero_visible), len(tablero_visible[0])
            direcciones = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

            for d_fila, d_columna in direcciones:
                nueva_fila, nueva_columna = fila + d_fila, columna + d_columna
                if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                    revelar_celda(tablero_visible, tablero_real, nueva_fila, nueva_columna, celdas_destapadas)

def marcar_celda(tablero_visible, fila, columna, celdas_marcadas):
    if tablero_visible[fila][columna] == ' ':
        tablero_visible[fila][columna] = 'M'
        celdas_marcadas.add((fila, columna))
    elif tablero_visible[fila][columna] == 'M':
        tablero_visible[fila][columna] = ' '
        celdas_marcadas.remove((fila, columna))

def verificar_victoria(filas, columnas, celdas_destapadas, num_minas):
    casillas_destapadas = filas * columnas - num_minas
    return len(celdas_destapadas) == casillas_destapadas

def jugar():
    filas = 8
    columnas = 8
    num_minas = 10

    tablero_real, tablero_visible, celdas_destapadas, minas = inicializar_tablero(filas, columnas, num_minas)
    celdas_marcadas = set()
    juego_terminado = False

    while not juego_terminado:
        imprimir_tablero(tablero_visible)

        print("\nMenú:")
        print("1. Revelar celda")
        print("2. Marcar celda")
        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == '1':
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna: "))

            if (fila < 0 or fila >= filas) or (columna < 0 or columna >= columnas):
                print("Posición no válida. Intente de nuevo.")
                continue

            if (fila, columna) in minas:
                print("¡Boom! Has perdido.")
                juego_terminado = True
            else:
                revelar_celda(tablero_visible, tablero_real, fila, columna, celdas_destapadas)

                if verificar_victoria(filas, columnas, celdas_destapadas, num_minas):
                    print("¡Felicidades! Has ganado.")
                    juego_terminado = True
        elif opcion == '2':
            fila = int(input("Ingrese la fila: "))
            columna = int(input("Ingrese la columna: "))

            if (fila < 0 or fila >= filas) or (columna < 0 or columna >= columnas):
                print("Posición no válida. Intente de nuevo.")
                continue

            marcar_celda(tablero_visible, fila, columna, celdas_marcadas)
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
