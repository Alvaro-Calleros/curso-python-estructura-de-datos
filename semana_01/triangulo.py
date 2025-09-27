res = 1
while (res ==1):
    base = float(input("teclea la base del triangulo: "))
    altura = float(input("teclea la altura del triangulo: "))
    area = (base * altura) / 2
    print("El área del triángulo es :", area)
    res = int(input("Teclea 1 para repetir el cálculo o 0 para salir: "))