from statistics import mode, median, mean
import random

# Trabajo Practico U 3 Comision 23

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print("Ejercicio 1 - Clasificación de edad")
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

print("Ejercicio 1 - Resultado por nota")
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar

print("Ejercicio 3 - Validación de número par")
numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

print("Ejercicio 4 - Categorías por edad")
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

print("Ejercicio 5 - Validación de contraseña")
password = input(
    "Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")

if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

# 6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

print("Ejercicio 6 - Sesgo de 50 números aleatorios")
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print("Caso inesperado")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

print("Ejercicio 7 - Obtenga su palabra con signo de exclamación si finaliza en vocal")
palabra = input("Ingrese una palabra: ")

if palabra[-1].lower() in "aeiouáéíóú":
    print(f"{palabra}!")
else:
    print(palabra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

print("Ejercicio 8 - Imprima su nombre en la capitalización indicada")
nombre = input("Ingrese su nombre: ")
capitalizacion = int(input(
    "Ingrese el número del formato deseado: 1 (mayúsculas), 2: (minúsculas), 3 (tipo título): "))
if capitalizacion == 1:
    print(nombre.upper())
elif capitalizacion == 2:
    print(nombre.lower())
elif capitalizacion == 3:
    print(nombre.title())
else:
    print("Formato seleccionado incorrecto")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Ejercicio 9 - Consulte la magnitud de un terremoto según la escala de Richter")
magnitud = int(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print('"Muy leve" (imperceptible)')
elif magnitud < 4:
    print('"Leve" (ligeramente perceptible)')
elif magnitud < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños)')
elif magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif magnitud < 7:
    print('"Muy Fuerte" (puede causar daños significativos)')
else:
    print('"Extremo" (puede causar graves daños a gran escala)')


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año                                 Estación en el hemisferio norte     Estación en el hemisferio sur

# Desde el 21 de diciembre hasta el 20 de         Invierno                            Verano
# marzo (incluidos)

# Desde el 21 de marzo hasta el 20 de junio       Primavera                           Otoño
# (incluidos)

# Desde el 21 de junio hasta el 20 de              Verano                             Invierno
# septiembre (incluidos)

# Desde el 21 de septiembre hasta el 20 de         Otoño                              Primavera
# diciembre (incluidos)

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print("Ejercicio 10 - Consulte la estación del año")
hemisferio = input(
    "Ingrese el hemisferio en el que se encuentra: N (norte) o S (sur): ")
mes = int(input("Ingrese el mes del año a consultar (en números): "))
dia = int(input("Ingrese el día del mes a consultar (en números): "))

# N S
# 1 al 12
# cambios 21-12, 21-03, 21-06, 21-09

if hemisferio not in ["S", "N"]:
    print("Hemisferio incorrecto")
elif not (0 < mes <= 12) or dia < 1:
    print("Fecha incorrecta")
elif mes == 2 and dia > 29 or mes in [4, 6, 9, 11] and dia > 30 or mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31:
    print("Fecha incorrecta")
elif mes in [1, 2] or mes == 12 and dia >= 21 or mes == 3 and dia < 21:
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
elif mes in [4, 5] or mes == 3 and dia >= 21 or mes == 6 and dia < 21:
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")
elif mes in [7, 8] or mes == 6 and dia >= 21 or mes == 9 and dia < 21:
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
elif mes in [10, 11] or mes == 9 and dia >= 21 or mes == 12 and dia < 21:
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")
