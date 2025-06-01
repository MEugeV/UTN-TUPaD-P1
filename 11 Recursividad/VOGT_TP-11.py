# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial_n(n):
    if n < 2:
        return 1
    return n * factorial_n(n-1)


def factorial_n_range():
    n = int(input("Ingrese el numero del cual desea calcular el factorial : "))
    for i in range(1, n + 1):
        print(f"El factorial de {i} es = {factorial_n(i)}")


factorial_n_range()


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci_n(n):
    if n <= 1:
        return n
    return fibonacci_n(n-1) + fibonacci_n(n-2)


def fibonacci_n_positions():
    n = int(input("Ingrese el numero de posiciones fibonacci que desea recibir: "))
    for i in range(n):
        print(f"La posicion Fibonacci {i} es = {fibonacci_n(i)}")


fibonacci_n_positions()

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 ^ 𝑚 = 𝑛 ∗ 𝑛 ^ (𝑚−1)
# . Prueba esta función en un
# algoritmo general.


def potencia(num, exponente):
    if exponente == 1:
        return num
    return num * potencia(num, exponente-1)


print(potencia(2, 4))  # => 16
print(potencia(3, 3))  # => 27
print(potencia(11, 6))  # => 1771561

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".


def decimal_a_binario(entero):
    if (entero // 2) < 2:
        return str(entero // 2) + str(entero % 2)
    return decimal_a_binario(entero // 2) + str(entero % 2)


print(decimal_a_binario(10))  # => 1010
print(decimal_a_binario(254))  # => 11111110
print(decimal_a_binario(28))  # => 11100

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) == 1:
        return True
    if len(palabra) == 2:
        return palabra[0] == palabra[1]
    return False if palabra[0] != palabra[-1] else es_palindromo(palabra[1:-1])


print(es_palindromo("neuqueN"))
print(es_palindromo("areera"))
print(es_palindromo("noes"))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:


def suma_digitos(n):
    return n if n < 10 else n % 10 + suma_digitos(n // 10)


print(suma_digitos(1234))  # → 10 (1 + 2 + 3 + 4)
print(suma_digitos(9))  # → 9
print(suma_digitos(305))  # → 8 (3 + 0 + 5)


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:

def contar_bloques(n):
    return 1 if n == 1 else n + contar_bloques(n-1)


print(contar_bloques(1))  # → 1 (1)
print(contar_bloques(2))  # → 3 (2 + 1)
print(contar_bloques(4))  # → 10 (4 + 3 + 2 + 1)


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:


def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    ultimo_numero = numero % 10
    es_igual = 1 if ultimo_numero == digito else 0
    return es_igual + contar_digito(numero // 10, digito)


print(contar_digito(12233421, 2))  # → 3
print(contar_digito(5555, 5))  # → 4
print(contar_digito(123456, 7))  # → 0
