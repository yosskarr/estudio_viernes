# Funciones básicas de la calculadora
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir entre cero."
    else:
        return x / y

def potencia(x, y):
    return x ** y

# Función para mostrar el menú
def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Sumar números")
    print("2. Restar números")
    print("3. Multiplicar números")
    print("4. Dividir números")
    print("5. Potencia (elevar un número)")
    print("6. Salir")

# Función principal de la calculadora
def calculadora():
    while True:
        mostrar_menu()
        
        # Obtener la operación del usuario
        operacion = input("Ingresa el número de la operación (1/2/3/4/5/6): ")
        
        if operacion == '6':
            print("¡Gracias por usar nuestra calculadora! ¡Hasta la próxima!")
            break
        
        # Verificar que la operación seleccionada sea válida
        if operacion not in ['1', '2', '3', '4', '5']:
            print("Opción no válida. Por favor elige una opción entre 1 y 5.")
            continue
        
        # Obtener los números para la operación
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor ingresa valores numéricos válidos.")
            continue
        
        # Realizar la operación seleccionada
        if operacion == '1':
            print(f"La suma de {num1} y {num2} es: {sumar(num1, num2)}")
        elif operacion == '2':
            print(f"La resta de {num1} y {num2} es: {restar(num1, num2)}")
        elif operacion == '3':
            print(f"La multiplicación de {num1} y {num2} es: {multiplicar(num1, num2)}")
        elif operacion == '4':
            print(f"La división de {num1} y {num2} es: {dividir(num1, num2)}")
        elif operacion == '5':
            print(f"La potencia de {num1} elevado a {num2} es: {potencia(num1, num2)}")
        
        # Preguntar si el usuario quiere hacer otro cálculo
        continuar = input("\n¿Quieres realizar otro cálculo? (s/n): ")
        if continuar.lower() != 's':
            print("¡Gracias por usar nuestra calculadora! ¡Hasta la próxima!")
            break

# Ejecutar la calculadora
calculadora()
