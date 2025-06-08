# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

lista_frutas = precios_frutas.keys()
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

print("Programa para almacenar y consultar numeros telefonicos")

agenda = {}

for i in range(5):
    nombre = input(f"Ingresa el nombre del {i+1}° Contacto: ")
    numero = input(f"Ingresa el número del {i+1}° Contacto: ")
    agenda[nombre] = numero

busqueda= input("Ingresa el nombre del contacto a buscar: ")
resultado =agenda[busqueda] if busqueda in agenda else ""
if resultado:
    print(f"Su numero es {resultado}")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresa una frase: ")
palabras_unicas = set(frase.split(" "))
print("palabras unicas", palabras_unicas)
diccionario_de_palabras = {}
for palabra in frase.split(" "):
     diccionario_de_palabras[palabra] = diccionario_de_palabras.get(palabra, 0) + 1
print("frecuencia de palabras", diccionario_de_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

diccionario_de_notas = {}

for i in range(3):
    nombre = input(f"Ingresa el nombre del {i+1}° Alumno: ")
    notas_str = input(f"Ingresa las tres notas del contacto separadas por coma: ")
    tupla_notas = tuple(int(n) for n in notas_str.split(","))
    diccionario_de_notas[nombre] = tupla_notas

for clave, valor in diccionario_de_notas.items():
    suma_notas = 0
    total_notas = 0
    for nota in valor:
        suma_notas += nota
        total_notas += 1
    print(f"El promedio del alumno {clave} es {suma_notas/total_notas}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

set_aprobados_primer_parcial = {1,2,4,5}
set_aprobados_segundo_parcial = {1,2,3,6,7,8,9}

aprobados_ambos_parciales = set_aprobados_primer_parcial.intersection(set_aprobados_segundo_parcial)
aprobados_un_solo_parcial = set_aprobados_primer_parcial.symmetric_difference(set_aprobados_segundo_parcial)
aprobados_al_menos_un_parcial = set_aprobados_primer_parcial.union(set_aprobados_segundo_parcial)

print("aprobados_ambos_parciales", aprobados_ambos_parciales)
print("aprobados_un_solo_parcial", aprobados_un_solo_parcial)
print("aprobados_al_menos_un_parcial", aprobados_al_menos_un_parcial)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock = {
    "cuadernos" : 1,
    "lapices": 2,
    "gomas": 4
}

accion =int(input("Ingrese el número de la accion a realizar: 1: consulta stock, 2: ingresar unidades: "))

if accion == 1:
    item = input("Ingrese el nombre del item a consultar: ")
    print( f"El item {item} tiene {stock[item]} unidades" if item in stock else "El item consultado no esta en stock")
elif accion == 2:
    item = input("Ingrese el nombre del item a cargar: ")
    cantidad = int(input("Ingrese la cantidad de unidades a ingresar: "))
    stock[item] = stock.get(item, 0) + cantidad

print(stock)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda_diaria = {
    ("lunes", 14) : "Gimnasia",
    ("lunes", 20): "Clase",
    ("martes",15) : "Trabajo",
    ("martes", 21) : "Centa"
} 

consulta = (input("Ingrese el día en texto y hora (sin minutos, en formato 24 hs) a consulta separados por coma: "))
fraccion_consulta = consulta.split(",")
dia_horario_consultado = (fraccion_consulta[0].strip().lower(), int(fraccion_consulta[1].strip()))

print( agenda_diaria[dia_horario_consultado] if dia_horario_consultado in agenda_diaria else "No tiene evenos en ese dia y horario")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

capitales = {
    "Francia": "Paris",
    "Italia": "Roma",
    "Berlin": "Alemania"
}

paises_de_capitales = {}

for clave, valor in capitales.items():
    paises_de_capitales[valor] = clave

print(paises_de_capitales)