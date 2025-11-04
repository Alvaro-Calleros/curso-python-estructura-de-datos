import lib_matrices_alvaro as lma
import keyboard
# import numpy as np
# # Crear una matriz de 3x3 con valores del 1 al 9
# matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Matriz original:")
# print(matriz)

# ----- Matrices sin numpy -----
x = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]


# lma.imprimir_matriz(x)

op = 1
while (op!=5):
    print("Menu de programas hechos con ciclos For")
    print("1. Capturar matriz")
    print("2. Imprimir matriz")
    print("3. Ordenar matriz Ascendentemente")
    print("4. Ordenar matriz Descendentemente")
    print("5. Escanear matriz (mostrar una por una las posiciones de la matriz)")
    print("6. Salir")

    op = int(input("Ingrese una opcion: "))
    
    if op == 1:
        x = lma.leer_matriz()
    elif op == 2:
        lma.imprimir_matriz(x)
    elif op == 3:
        lma.ordenar_matriz_ac(x)
        print("Matriz ordenada acendentemente, Selecciona la opcion 2 para verlo")
    elif op == 4:
        lma.ordenar_matriz_de(x)
        print("Matriz ordenada descendentemente, Selecciona la opcion 2 para verlo")
    elif op == 5:
        while(1>0):
            if keyboard.is_pressed('q'):  
                break
            lma.escanear_mat(x)
    elif op == 6:
        print("Saliendo del programa...")
    else:
        print("Opcion no valida, intente de nuevo.")
    print()  
    
    