import math
# Ejercicio 1


def imprimir_hola_mundo():
    print("Hola Mundo!")

# Ejercicio 2


def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Ejercicio 3


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejercicio 5


def segundos_a_horas(segundos):
    seg_per_min = 60
    min_per_hour = 60
    return segundos / (seg_per_min * min_per_hour)

# Ejercicio 6


def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i}  = {i*numero}")


# Ejercicio 7


def operaciones_basicas(a, b):
    suma = a + b
    resta = a-b
    division = a / b
    multiplicacion = a * b
    return (suma, resta, division, multiplicacion)

# Ejercicio 8


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Ejercicio 9


def celsius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32

# Ejercicio 10


def calcular_promedio(a, b, c):
    return (a+b+c)/3

# Funciones modularizadas para devolver un número en ingresos del usuario


def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False


def int_input(message):
    numero = input(message)
    if es_entero(numero):
        return int(numero)
    else:
        return int_input(message)


def es_decimal(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def float_input(message):
    numero = input(message)
    if es_decimal(numero):
        return float(numero)
    else:
        return float_input(message)


# Ejecución ejercicio 1
imprimir_hola_mundo()

# Ejecución ejercicio 2
nombre = input("Ingresa tu nombre: ")
saludar_usuario(nombre)

# Ejecución ejercicio 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# Ejecución ejercicio 4
radio = float_input("Ingrese el radio de un círculo: ")

print(f"El área del círculo es {calcular_area_circulo(radio)}")
print(f"El perimetro del círculo es {calcular_perimetro_circulo(radio)}")

# Ejecución ejercicio 5
segundos = float_input("Ingrese los segundos a convertir en horas: ")

print(
    f"Las horas correspondientes a {segundos} segundos son {segundos_a_horas(segundos)} horas")

# Ejecución ejercicio 6
numero = int_input(
    "Ingresa un número entero para obtener su tabla de multiplicar: ")

tabla_multiplicar(numero)

# Ejecución ejercicio 7
numero_1 = 6
numero_2 = 3

(suma, resta, division, multiplicacion) = operaciones_basicas(numero_1, numero_2)

print(
    f"Los resultados de las operaciones de los números {numero_1} y {numero_2} son : suma = {suma}, resta = {resta}, división = {division}, multiplicación = {multiplicacion}")

# Ejecución ejercicio 8
peso = float_input("Ingrese su peso en kg: ")
estatura = float_input("Ingrese su estatura en mt: ")
print(f"Su IMC es {round(calcular_imc(peso, estatura), 2)}")


# Ejecucion ejercicio 9
celsius = float_input("Ingrese la temperatura en celcius: ")

print(
    f"La temperatura en farentheit correspondiente a {celsius} grados celius es {celsius_a_fahrenheit(celsius)}")

# Ejecución ejercicio 10
numero_1 = float_input("Ingrese el primer número: ")
numero_2 = float_input("Ingrese el segundo número: ")
numero_3 = float_input("Ingrese el tercer número: ")

print(
    f"El promedio de los tres números {numero_1}, {numero_2} y {numero_3} es {calcular_promedio(numero_1, numero_2, numero_3)}")
