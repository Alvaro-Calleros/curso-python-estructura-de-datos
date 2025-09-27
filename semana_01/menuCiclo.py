import lib_alvaro

op = 0

while (op!=4):
    print("Menu de programas hechos con ciclos For")
    print("1. Programa Tablas")
    print("2. Programa suma de 2 numeros")
    print("3. Programa ...")
    print("4. Salir")
    
    op = int(input("Ingrese una opcion: "))
    
    if op == 1:
        lib_alvaro.tablas()
        
    elif op == 2:
        x = int(input("Ingrese el primer numero: "))
        y = int(input("Ingrese el segundo numero: "))
        res = lib_alvaro.suma_dos_numeros(x,y)
        print(res)
    elif op == 3:
        print("Opcion 3")
        # lib_alvaro.programa3()
    elif op == 4:
        print("Hasta la vista, baby...")
    else:
        print("Opcion no valida, intente de nuevo.")
    print()  
    
    