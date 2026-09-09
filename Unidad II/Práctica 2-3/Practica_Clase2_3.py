#Practica de ejercicios Bucles y funciones, listas y tuplas, estructura de datos. 

#BUCLE FOR

"""
INSTRUCCIÓN, PARTE A
Con la lista horas_estudio = [2, 3, 1, 4, 2, 5, 3] (horas estudiadas cada día de la semana), 
calcula e imprime el total de horas estudiadas y el promedio diario, redondeado a 1 decimal.
No copies el ejemplo de la clase con edades y un contador de mayores de 30.
Aquí son horas de estudio, y el primer cálculo es una suma total, no un conteo.
"""
Horas_estudio = [2, 3, 1, 4, 2, 5, 3]

Total_horas = 0

for hora in Horas_estudio:
    Total_horas += hora

promedio = round(Total_horas / len(Horas_estudio), 1)

print("Total de horas estudiadas:", Total_horas)
print("Promedio diario:", promedio)

"""
INSTRUCCIÓN, PARTE B
Usando la misma lista, cuenta cuántos días estudiaste 3 horas o más, con una variable contadora.

SOLUCIÓN, PARTE B
"""

Horas_estudio = [2, 3, 1, 4, 2, 5, 3]

Contador = 0

for hora in Horas_estudio:
    if hora >= 3:
        Contador += 1

print("Días con 3 horas o más:", Contador)

#BUCLE WHILE

"""
INSTRUCCIÓN
Simula un plan de ahorro: empiezas con $0 y ahorras $45 cada semana.
Usa while para saber cuántas semanas completas necesitas para alcanzar al menos $300,
e imprime el número de semanas y el ahorro final acumulado. 
"""

Ahorro = 0
Semanas = 0

# Vamos sumando semana por semana hasta llegar a la meta
while Ahorro < 300:
    Semanas = Semanas + 1
    Ahorro = Ahorro + 45

print("Total de semanas:", Semanas)
print("Monto acumulado:", Ahorro)

#FUNCIONES

"""
INSTRUCCIÓN, PARTE A
Escribe una función calcular_costo_envio(peso, distancia) que calcule el costo de un envío
con la fórmula: peso * 0.5 + distancia * 0.1. Llámala con un paquete de 12 kg que viaja 80 km,
e imprime el resultado redondeado a 2 decimales.
"""

def calcular_costo_envio(peso, distancia):
    return round(peso * 0.5 + distancia * 0.1, 2)


costo = calcular_costo_envio(12, 80)
print("Costo del envío:", costo)

"""
INSTRUCCIÓN, PARTE B
Escribe una segunda función clasificar_envio(costo) que reciba un costo y devuelva
"Económico" si es menor a 10, "Estándar" si es de 10 a 24.99, y "Premium" si es 25 o más.
Llámala con el resultado de la parte A.
"""

def clasificar_envio(costo):
    if costo < 10:
        return "Económico"
    elif costo < 25:
        return "Estándar"
    else:
        return "Premium"

clasificacion = clasificar_envio(costo)
print("Clasificación del envío:", clasificacion)

"""
INSTRUCCIÓN, PARTE A
Con la lista peliculas de 6 títulos, imprime la lista completa,
la primera película, la última (con índice negativo),
las primeras 3 (con slicing),
y cuántas películas hay en total.
"""
peliculas = ["El Padrino", "La Lista de Schindler", "El Señor de los Anillos", "Star Wars", "Matrix", "El Rey León"]

print("Lista completa:", peliculas)
print("Primera película:", peliculas[0])
print("Última película:", peliculas[-1])
print("Primeras 3 películas:", peliculas[:3])
print("Total de películas:", len(peliculas))

"""
INSTRUCCIÓN, PARTE B
Usando slicing con paso, imprime las películas en las posiciones pares (0, 2, 4).
Después imprime las películas desde la posición 1 hasta la 3 (sin incluir la 4).
"""
print("Películas en posiciones pares:", peliculas[::2])
print("Películas desde la posición 1 hasta la 3:", peliculas[1:4])

#METODO DE LISTAS

"""
INSTRUCCIÓN
Empieza con carrito = ["pantalon", "camisa"]. Agrega "zapatos" al final, agrega "cinturon" en la posición 1, quita "pantalon". 
Verifica si "camisa" sigue en el carrito, y por último ordena el carrito alfabéticamente.Imprime el carrito después de cada paso.
"""
carrito = ["pantalon", "camisa"]
carrito.append("zapatos")
print("Carrito después de agregar zapatos:", carrito)
carrito.insert(1, "cinturon")
print("Carrito después de agregar cinturon en la posición 1:", carrito)
carrito.remove("pantalon")
print("Carrito después de quitar pantalon:", carrito)
if "camisa" in carrito:
    print("Camisa sigue en el carrito.")

#LISTAS ANIDADAS
"""
INSTRUCCIÓN, PARTE A
Con el mapa de asientos asientos (una cuadrícula 3×3 de "L" libre / "X" ocupado),
imprime la primera fila completa,
el asiento en la fila 1 columna 2,
y luego recorre todas las filas con un for para imprimir cada una.
"""
asientos = [["L", "X", "L"],
            ["X", "L", "X"],
            ["L", "X", "L"]]

print("Primera fila completa:", asientos[0])
print("Asiento en la fila 1 columna 2:", asientos[1][2])
print("Mapa de asientos:")
for fila in asientos:
    print(fila)

"""
INSTRUCCIÓN, PARTE B
Con ventas_vendedores (nombre + 3 ventas por vendedor), calcula e imprime, para cada vendedor, su nombre y el total de sus ventas.
"""
ventas_vendedores = [
    ["Juana", 100, 150, 200],
    ["Carlos", 120, 180, 220],
    ["Rodrigo", 90, 140, 190]
]

for vendedor in ventas_vendedores:
    nombre = vendedor[0]
    total_ventas = sum(vendedor[1:4])
    print(f"{nombre}: ${total_ventas}")

#TUPLAS
"""
INSTRUCCIÓN, PARTE A
Crea una tupla color = (120, 200, 50) que representa un color en RGB.
Imprímela completa, cada canal por separado, y su type().
"""
color = (120, 200, 50)
print("Tupla completa:", color)
print("Canal rojo:", color[0])
print("Canal verde:", color[1])
print("Canal azul:", color[2])
print("Tipo de dato:", type(color))

"""
INSTRUCCIÓN, PARTE B
Usa una función calcular_brillo(c) que devuelva el promedio de los 3 canales de un color,
para comparar color_a = (120, 200, 50) contra color_b = (10, 10, 10)
e imprimir cuál es más brillante.
"""

def calcular_brillo(c):
    return sum(c) / len(c)

color_a = (120, 200, 50)
color_b = (10, 10, 10)

brillo_a = calcular_brillo(color_a)
brillo_b = calcular_brillo(color_b)

if brillo_a > brillo_b:
    print("El color A es más brillante.")
elif brillo_a < brillo_b:
    print("El color B es más brillante.")
else:
    print("Ambos colores tienen el mismo brillo.")  


"""
DESAFÍO FINAL
Torneo de trivia por equipos

INSTRUCCIÓN
Vas a recibir una lista de equipos, donde cada equipo es una lista con el nombre seguido de 3 puntajes de ronda; por ejemplo: ["Los Rayos", 15, 20, 18]. Con esa lista de equipos, tu programa debe:

1. Con un for, calcular el total de puntos de cada equipo (la suma de sus 3 rondas) e imprimir, para cada uno, su nombre, su total, y su clasificación.

2. Escribir una función clasificar_equipo(total) que devuelva "Campeón" si el total es 60 o más, "Finalista" si es de 40 a 59, y "Participante" si es menor a 40.

3. Encontrar cuál equipo tiene el total más alto.

4. Con un while, simular una ronda bonus para ese equipo: cada vuelta suma 5 puntos extra hasta que su total llegue o supere los 70 puntos. Contar cuántas rondas bonus tomó, e imprimir el nombre del equipo, las rondas necesarias, y el total final tras la ronda bonus.

5. Guardar el resultado del campeonato en una tupla (nombre, clasificación) con el nombre del equipo que tuvo el total más alto y su clasificación, e imprimirla.

Si el equipo con más puntos ya tiene 70 o más desde el inicio, el while de la ronda bonus simplemente no debería entrar ninguna vez: 0 rondas es una respuesta válida.
"""

#LISTAS

# equipos = [
#     ["Los Rayos", 15, 20, 18],
#     ["Estrellas FC", 22, 19, 25],
#     ["Team Nova", 10, 12, 8],
# ]

equipos = [
    ["Halcones", 12, 14, 10],
    ["Titanes", 30, 28, 15],
    ["Fénix", 18, 16, 20],
]


#FUNCIONES
def clasificar_equipo(total):
    if total >= 60:
        return "Campeón"
    elif total >= 40:
        return "Finalista"
    else:
        return "Participante"

totales = [] 
for equipo in equipos:
    nombre = equipo[0]
    total = equipo[1] + equipo[2] + equipo[3]
    categoria = clasificar_equipo(total)

    print(f"{nombre}: total {total}, {categoria}")
    totales.append([nombre, total])


mayor_equipo = None
mayor_total = -1

for nombre, total in totales:
    if total > mayor_total:
        mayor_total = total
        mayor_equipo = nombre

print("Equipo con más puntos:", mayor_equipo)


#WHILE
bonus = 0
total_final = mayor_total
while total_final < 70:
    total_final += 5
    bonus += 1
print("Rondas bonus necesarias:", bonus)
print("Total final tras ronda bonus:", total_final)

#TUPLA
resultado_final = (mayor_equipo, clasificar_equipo(mayor_total))
print("Resultado final:", resultado_final)