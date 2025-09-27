def table():
    try:
        base = int(input("teclea la tabla que deseas calcular: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    for i in range(1, 11):
        print(f"{base} x {i} = {base * i}")
    print("Adiós")

def all_tables():
    for base in range(1, 11):
        print(f"Tabla del {base}:")
        for i in range(1, 11):
            print(f"{base} x {i} = {base * i}")
        print()  # Línea en blanco entre tablas
    print("Adiós")

def menu():
    while True:
        print("Menu:")
        print("1. Calcular tabla de multiplicar específica")
        print("2. Calcular todas las tablas de multiplicar del 1 al 10")
        print("0. Salir")
        try:
            res = int(input("Teclea tu opción (0-2): "))
        except ValueError:
            print("Por favor, ingresa una opción válida (0-2).")
            continue
        if res == 0:
            print("Adiós")
            break
        elif res == 1:
            table()
        elif res == 2:
            all_tables()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()