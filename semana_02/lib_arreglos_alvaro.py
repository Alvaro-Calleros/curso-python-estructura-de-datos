
def leer_arreglo(arreglo):
    for i in range(0, 5, 1):
        arreglo[i] = int(input(f"Ingrese el valor del arreglo en {i+1}: "))
    return arreglo

def imprimir_arreglo(arreglo):
    for i in range(0, 5, 1):
            print(arreglo[i])

def ordenar_arreglo_ac(arreglo):
    for i in range(0, 4, 1):
        for j in range(0, 4-i, 1): # restamos el contador en i para no comparar los valores ya ordenados
            # asi la complejidad baja de O(n^2) a logarítmica O(n log n)
            if arreglo[j] > arreglo[j+1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = temp
    return arreglo

def ordenar_arreglo_de(arreglo):
    for i in range(0, 4, 1):
        for j in range(0, 4-i, 1):
            if arreglo[j] < arreglo[j+1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = temp
    return arreglo