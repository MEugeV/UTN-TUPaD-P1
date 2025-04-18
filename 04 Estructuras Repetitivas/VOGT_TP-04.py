# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

import random
print("Ejercicio 1 - Imprime números del 1 al 100")

for num in range(101):
    print(num)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

print("Ejercicio 2 - Cantidad de dígitos del entero")

number_string = input("Ingrese un número entero: ")
# Valido si el valor ingresado es un número, eliminando el signo negativo el inicio para poder
# aplicar el método isdigit
absolute_value_number_string = number_string[1:] if number_string.startswith(
    "-") else number_string
# Si el string es un número entero, transformo el string a número y lo divido sucesivamente por diez
# y utilizo un acumulador para contar los dígitos
if absolute_value_number_string.isdigit():
    number = int(absolute_value_number_string)
    count = 1
    while number >= 10:
        number /= 10
        count += 1
    print(f"El número ingresado tiene {count} dígitos")
# Si el string ingresado no es un entero, lo comunico al usuario
else:
    print("El valor ingresado no es un número entero")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("Ejercicio 3 - Suma de valores en entre dos números sin incluirlos")

first_number = int(input("Ingrese un número entero: "))
second_number = int(input("Ingrese un segundo número entero: "))

sum = 0
for number in range(first_number + 1, second_number):
    sum += number
print(f"Los valores comprendidos entre ambos números suman: {sum}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

print("Ejercicio 4 - Suma de enteros")

sum = 0
numero = 1
while numero != 0:
    numero = int(
        input("Ingrese un número entero a sumar (para finalizar la suma ingrese 0): "))
    sum += numero
print(f"Los números ingresados suman {sum}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


print("Ejercicio 5 - Adivine el número aleatorio")


count = 0
random_number = random.randint(0, 9)
guessed_number = 10
while guessed_number != random_number:
    guessed_number = int(input("Ingrese un número entre 0 y 9: "))
    count += 1
print(
    f"El número era {random_number} . El número de intentos realizados para adivinar el número fue {count}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

print("Ejercicio 6 - Rango decreciente de número pares 100 a 0")

for number in range(100, -1, -2):
    print(number)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

print("Ejercicio 7 - Suma acumulada desde cero")

numero_string = input("Ingrese un número entero positivo: ")
if numero_string.isdigit():
    sum = 0
    for numero in range(0, int(numero_string) + 1):
        sum += numero
    print(
        f"La suma de los valores de 0 a {numero_string} inclusive es igual a {sum}")
else:
    print("El número ingresado no es un número entero positivo")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numbers_quantity = 100
print(
    f"Ejercicio 8 - Clasificación de {numbers_quantity} números ingresados en pares, impares, negativos y positivos")

pares = 0
positivos = 0

for number in range(numbers_quantity):
    value = int(input("Ingrese el siguiente valor :"))
    if value % 2 == 0:
        pares += 1
    if value >= 0:
        positivos += 1

print(
    f"El total de números pares es: {pares}, impares es: {numbers_quantity-pares}, positivos es: {positivos} y negativos es {numbers_quantity-positivos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

numbers_quantity = 100
print(
    f"Ejercicio 9 - Cálculo de media de {numbers_quantity} números ingresados")

sum = 0

for number in range(numbers_quantity):
    value = int(input("Ingrese el siguiente valor :"))
    sum += value

print(
    f"La media de los valores ingresados es: {sum/numbers_quantity}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("Ejercicio 10 - Inversión de dígitos del entero")

numero_string = input("Ingrese un número entero: ")

if numero_string.isdigit():
    numero_invertido = ""
    for position in range(len(numero_string)-1, -1, -1):
        numero_invertido += numero_string[position]
    print(f"El número invertido del valor ingresado es {numero_invertido}")
# Si el string ingresado no es un entero, lo comunico al usuario
else:
    print("El valor ingresado no es un número entero")
