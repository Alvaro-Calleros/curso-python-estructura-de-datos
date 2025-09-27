opc = 1
n = 0
while opc == 1:
    x = 1
    n = int(input("Teclea un número para verificar si es primo: "))
    if n <= 1:
        x = 0
    else:
        for i in range(2, n, 1): 
            if n % i == 0:
                x = 0
    if x == 1:
        print(f"{n} es un número primo.")
    else:
        print(f"{n} no es un número primo.")
    opc = int(input("Teclea 1 para verificar otro número o 0 para salir: "))
print("Adiós")