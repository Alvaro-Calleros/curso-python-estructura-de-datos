import math

def calculator_add(a, b):
    return a + b

def calculator_subtract(a, b):
    return a - b

def calculator_multiply(a, b):
    return a * b

def calculator_divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"

def calculator_power(a, b):
    return a ** b

def calculator_modulus(a, b):
    return a % b

def calculator_square_root(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Square root of negative number error"

def calculator_factorial(n):
    if n < 0:
        return "Factorial of negative number error"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def calculator_logarithm(a, base=10):
    if a > 0 and base > 1:
        return math.log(a, base)
    else:
        return "Logarithm error: a must be > 0 and base must be > 1"

def calculator_sine(angle):
    return math.sin(math.radians(angle))

def calculator_cosine(angle):
    return math.cos(math.radians(angle))

def calculator_tangent(angle):
    return math.tan(math.radians(angle))

def calculator_hypotenuse(a, b):
    return math.hypot(a, b)

def menu():
    print("\nWelcome to the Calculator Module")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Logarithm")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")
    print("13. Hypotenuse")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (0-13): ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Result:", calculator_add(a, b))
        elif choice == "2":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Result:", calculator_subtract(a, b))
        elif choice == "3":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Result:", calculator_multiply(a, b))
        elif choice == "4":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Result:", calculator_divide(a, b))
        elif choice == "5":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Result:", calculator_power(a, b))
        elif choice == "6":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Result:", calculator_modulus(a, b))
        elif choice == "7":
            a = float(input("a: "))
            print("Result:", calculator_square_root(a))
        elif choice == "8":
            n = int(input("n: "))
            print("Result:", calculator_factorial(n))
        elif choice == "9":
            a = float(input("a: "))
            base = float(input("base (default 10): ") or "10")
            print("Result:", calculator_logarithm(a, base))
        elif choice == "10":
            angle = float(input("angle (degrees): "))
            print("Result:", calculator_sine(angle))
        elif choice == "11":
            angle = float(input("angle (degrees): "))
            print("Result:", calculator_cosine(angle))
        elif choice == "12":
            angle = float(input("angle (degrees): "))
            print("Result:", calculator_tangent(angle))
        elif choice == "13":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Result:", calculator_hypotenuse(a, b))
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()