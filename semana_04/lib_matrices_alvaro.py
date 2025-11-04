
import os
from time import time


def imprimir_matriz(matriz):
    for i in range(0, len(matriz), 1):
        print(matriz[i])
        
        
def leer_matriz():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    
    return matriz

def ordenar_matriz_ac(matriz): ##fuerza bruta pero funciona XD, 0(n^4)
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    
    for i in range(filas):
        for j in range(columnas):
            for k in range(filas):
                for l in range(columnas):
                    if matriz[i][j] < matriz[k][l]:
                        temp = matriz[i][j]
                        matriz[i][j] = matriz[k][l] 
                        matriz[k][l] = temp
    return matriz

def ordenar_matriz_de(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0

    for i in range(filas):
        for j in range(columnas):
            for k in range(filas):
                for l in range(columnas):
                    if matriz[i][j] > matriz[k][l]:
                        temp = matriz[i][j]
                        matriz[i][j] = matriz[k][l] 
                        matriz[k][l] = temp
    return matriz

import time  # Asegúrate de importar time

def escanear_mat(x):
    filas = len(x)
    columnas = len(x[0]) if filas > 0 else 0
    for i in range(filas):
        for j in range(columnas):
            aux = x[i][j]
            x[i][j] = '@'
            imprimir_matriz(x)
            time.sleep(1)
            x[i][j] = aux
            os.system('cls')