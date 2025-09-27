opc = 1
tabla = 0

while (opc !=0):
    opc = int(input("Opcion: 0: salir, 1: tabla especifica: "))
    if opc == 1:
        tabla = int(input("teclea la tabla que deseas calcular: "))
        for i in range(1, 11):
            print(f"{tabla} x {i} = {tabla * i}")
        
print("Adiós")