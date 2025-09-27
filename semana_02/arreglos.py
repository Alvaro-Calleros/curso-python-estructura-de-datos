import lib_arreglos_alvaro

op = 0

x = [0, 0, 0, 0, 0]

while (op!=5):
    print("Menu de programas hechos con ciclos For")
    print("1. Capturar Arreglo")
    print("2. Imprimir Arreglo")
    print("3. Ordenar Arreglo Ascendentemente")
    print("4. Ordenar Arreglo Descendentemente")
    print("5. Salir")

    op = int(input("Ingrese una opcion: "))
    
    if op == 1:
        lib_arreglos_alvaro.leer_arreglo()
    elif op == 2:
        lib_arreglos_alvaro.imprimir_arreglo(x)
    elif op == 3:
        lib_arreglos_alvaro.ordenar_arreglo_ac(x)
        print("Arreglo ordenado acendentemente, Selecciona la opcion 2 para verlo")
    elif op == 4:
        lib_arreglos_alvaro.ordenar_arreglo_de(x)
        print("Arreglo ordenado descendentemente, Selecciona la opcion 2 para verlo")
    elif op == 5:
        print("Hasta la vista, baby...")
    else:
        print("Opcion no valida, intente de nuevo.")
    print()  
    
    