# metodo para agregar elementos a la lista
frutas = ["manzana", "pera", "uva", "sandia"]
print(frutas)
print(frutas[-1])
print(frutas[1:3])
print(len(frutas))

frutas.append("mango")
print(frutas)


# metodo para eliminar elementos de la lista
frutas.remove("banana")
print(frutas)


# metodo para insertar valores en un lugar especifico dentro de la lista
frutas.insert(1, "toronja")
print(frutas)


# preguntar si existe un elemento dentro de la lista
print("naranja" in frutas)
print("mandarina" in frutas)

# metodo para organizar la lista de menor a mayor
numeros_desordenados = [5, 2, 7, 1, 8]
orden_2 = sorted(numeros_desordenados)
orden = sorted(numeros_desordenados, reverse=True)
print("lista original:", numeros_desordenados)
print("lista ordenada: (de menor a mayor)", orden_2)
print("lista ordenada: (de mayor a menor)", orden)

# operaciones con lista de numeros
numeros = [10, 20, 30, 40, 50]
print(numeros[:2])
print(numeros[2:])
print(numeros[::2])


# ejercicio guiado I
temperaturas = [22, 25, 20, 32, 19, 27, 24]

print("Primeras 3:", temperaturas[:3])
print("Ultima", temperaturas[-1])

temp_max = max(temperaturas)
temp_min = min(temperaturas)

print("Maxima:", temp_max, "Minima:", temp_min)

# ejercicio guiado II
tareas = ["estudiar", "hacer ejercicio"]

# agregar el elemento "leer" a la lista
tareas.append("leer")

# agregar el elemento "cocinar" en la primera posicion de la lista
tareas.insert(1, "cocinar")

# eliminar el elemento "hacer ejercicio" de la lista
tareas.remove("hacer ejercicio")

# mostrar los elementos de la lista
print(tareas)

# preguntar si el elemento "estudiar" existe dentro de la lista
print("estudiar" in tareas)
# Listas aisladas
tablero = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]

# print(tablero[0])
# print(tablero[0][1])
print(tablero[2][2])

# ejercicio guiado
notas_estudiantes = [
    ["Esther", 85, 90, 78],
    ["Erick", 60, 70, 65],
]

for estudiante in notas_estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1:]
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio {round(promedio, 1)}")

# Tuplas
coordenada = (19.78, -70.69)

print(coordenada)
print(coordenada[0], coordenada[1])
print(type(coordenada))


# ejercicio guiado IV.
"""
calculen la distancia entre ambos puntos utilizando la formula para calcular distancias.

pista para calcular distancia utilice esta formula:
raiz cuadrada de ((x2-x1)2 + (y2-y1)2)

nota: para calcular la raiz cuadrada en python utilice ** 0.5
"""
punto_a = (0, 0)
punto_b = (3, 4)

x1, y1 = punto_a
x2, y2 = punto_b

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("La distancia entre los puntos es:", distancia)
