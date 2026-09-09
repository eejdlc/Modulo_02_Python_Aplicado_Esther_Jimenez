# crear diccionario
estudiante = {'nombre': 'Jefte', 'edad': 55, 'curso': 'IA'}

# verificar informacion del diccionario
print(estudiante['nombre'])

# modificar informacion del diccionario
estudiante['edad'] = 35
print(estudiante)

# agregar informacion al diccionario
estudiante['ciudad'] = "Santo Domingo"
print(estudiante)

# eliminar informacion del diccionario
del estudiante['curso']
print(estudiante)

"""
EJERCICIO PRACTICO

1. crear un diccionario llamado "producto"
2. las llaves (clave y valor) "nombre", "precio" y "stock"
3. agregar una nueva llave llamada "categoria"
4. modificar el valor de la llave "precio" sumandole 10 al valor original.
"""
producto = {"nombre": "Computadora", "precio": 400, "stock": 7}
print(producto)

producto["categoria"] = "Electronica"
print(producto)

producto["precio"] = producto["precio"] + 10
print(producto)

del producto["stock"]
print(producto)

# metodos para trabajar con diccionarios
print(estudiante.keys()) # devuelve todas las llaves del diccionario
print(estudiante.values()) # devuelve todos los valores del diccionario
print(estudiante.items()) # devuelve cada par clave:valor como si fuera una tupla

# acceder a un valor en el diccionario de manera segura
print(estudiante.get("edad"))
print(estudiante.get("telefono"))


"""
EJERCICIO GUIADO

utilicen este diccionario: "inventario = {"manzana": 50, "peras": 30, "uvas": 80}.
recorrer el diccionario con el metodo .items() que me imprima(print()) para cada producto si el stock es suficiente o no.

suficiente = 40 o mas
pocas - (insuficientes) = menos 40

"""
inventario = {"manzana": 50, "peras": 30, "uvas": 80}

for producto, cantidad in inventario.items():
    if cantidad > 40:
        print(f"{producto}: suficientes ({cantidad})")
    else:
        print(f"{producto}: pocas ({cantidad})")

# conjuntos (set)
frutas_emmy = {"manzanas", "pera", "uva"}

lista_valores_repetidos = ["manzanas", "pera", "uva", "manzanas", "pera"]

nueva_lista = set(lista_valores_repetidos)

print(nueva_lista)

# operaciones entre conjuntos
frutas_emmy = {"manzanas", "pera", "uva"}
frutas_mairon = {"banana", "uva", "pera"}

# juntar conjuntos sin repetir los valores que estan en los dos
print(frutas_emmy.union(frutas_mairon))

# devolver solo los valores que estan en ambos conjuntos a la vez
print(frutas_emmy.intersection(frutas_mairon))

"""
EJERCICIO GUIADO

trabajar con esta lista: respuesta = ["python", "java", "python", "C++", "python", "java"]

1. obtener cuantas respuestas distintas hay (sin repetir)
2. imprimir el numero de elementos que no se repiten en la lista, junto con el set de opciones distintas y ordenadas alfabeticamente

pista: transformar lista a set
"""
respuesta = ["python", "java", "python", "C++", "python", "java"]

respuesta_set = set(respuesta)

print("cantidad de respuestas distintas:", len(respuesta_set))
print("orden alfabetico:", sorted(respuesta_set))







