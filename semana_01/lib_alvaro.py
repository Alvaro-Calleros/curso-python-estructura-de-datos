def tablas():
    print("Hola, soy Una calculadora de tablas de multiplicar")
    tabla = int(input("teclea la tabla que deseas calcular: "))
    for i in range(1, 11):
    
        print(f"{tabla} x {i} = {tabla * i}")

def suma_dos_numeros(x, y):
    suma = x + y
    return f"La suma de {x} + {y} es: {suma}"
