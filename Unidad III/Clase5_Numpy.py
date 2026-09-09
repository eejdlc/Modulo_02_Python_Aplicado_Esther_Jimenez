import numpy as np

numeros = [10, 20, 30, 40, 50]
arreglo = np.array(numeros)

print(arreglo)
print(type(arreglo))

# operaciones vectorizadas
lista_normal = [1, 2, 3, 4, 5]
arreglo_numpy = np.array([1, 2, 3, 4, 5])

print(lista_normal * 2)
print(arreglo_numpy * 2)

"""
EJERCICIO GUIADO

1. crear un array llamado "precios"
2. introducir 5 precios de productos.
3. aplicar 15% de descuento a todos a la vez (multiplicar por 0.85)
4. redondear el resultado a 2 decimales

nota: no puede utilizar ningun bucle
"""
precios = np.array([100, 200, 300, 400, 500])
precios_descuento = precios * 0.85
precios_descuento_redondeados = np.round(precios_descuento, 2)
print(precios_descuento_redondeados)

# indexing, slicing, funciones estadísticas
temperaturas = np.array([25.9, 40.5, 15.7, 60.2, 33.2, 27.6, 24.3])

print(temperaturas[0])
print(temperaturas[-1])
print(temperaturas[2:5])

print('Promedio:', round(np.mean(temperaturas), 2))
print('Promedio:', np.mean(temperaturas).round(2))

print("maxima:", np.max(temperaturas))
print("minimo:", np.min(temperaturas))
print("sumar:", np.sum(temperaturas))
print("desviacion estandar:", np.std(temperaturas))

"""
EJERCICIO GUIADO
1. crear su propio array, llamarlo "temperaturas_semana"
2. introducir 7 valores a su array.
3. imprimir el promedio, la maxima, la mínima y la desviacion estandar
4. redondear todo los resultados a 1 decimal
"""
temperaturas_semana = np.array([25.9, 40.5, 15.7, 60.2, 33.2, 27.6, 24.3])
print('Promedio:', np.mean(temperaturas_semana).round(1))
print("maxima:", np.max(temperaturas_semana).round(1))
print("minimo:", np.min(temperaturas_semana).round(1))
print("desviacion estandar:", np.std(temperaturas_semana).round(1))

# Arrays de 2 dimensiones
matriz = np.array([
    [90, 85, 78],
    [70, 88, 92],
])

print(matriz)
print(matriz.shape)
print(matriz[0])
print(matriz[0][1])
print(matriz[1, 2])

print(np.mean(matriz, axis=1))  # calcula filas
print(np.mean(matriz, axis=0))  # calcula columnas

"""
EJERCICIO GUIADO
sacar el promedio de cada mes entre todas las sucursales utilizando la matriz "ventas"
"""

ventas = np.array([
    [1220, 1500, 1350],
    [980, 1300, 1050],
    [1600, 1440, 1700]
])

print("Promedio por sucursal:", np.mean(ventas, axis=1))
print("Promedio por mes:", np.mean(ventas, axis=0))