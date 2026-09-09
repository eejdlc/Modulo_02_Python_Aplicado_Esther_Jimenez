#ARRAYS: CREACION E INDEXADO

"""
INSTRUCCIÓN:
Crea un array calificaciones con 6 notas de examen (invéntalas).
Imprime la primera nota, la última, y las notas de la posición 2 a la 5 (sin incluir la 5).
Imprime también cuántas notas hay en total.
"""
import numpy as np

calificaciones = np.array([8, 9, 7, 10, 6, 8])
print("Primera nota:", calificaciones[0])
print("Última nota:", calificaciones[-1])
print("Notas de la posición 2 a la 5 (sin incluir la 5):", calificaciones[2:5])
print("Total de notas:", len(calificaciones))

#OPERACIONES VECTORIZADAS

"""
INSTRUCCIÓN:
Crea un array comisiones con 4 montos de comisión de ventas (invéntalos).
Aplica un bono del 10% a todas a la vez (multiplica por 1.10), sin usar ningún bucle,
y redondea el resultado a 2 decimales.
"""
comisiones = np.array([100, 200, 150, 250])
comisiones_bonificadas = np.round(comisiones * 1.10, 2)
print("Comisiones originales:", comisiones)
print("Comisiones con bono del 10%:", comisiones_bonificadas)

#FUNCIONES ESTADISTICAS

"""
INSTRUCCIÓN:
Crea un array consumo_gb con el consumo de datos móviles (en GB) de 7 días distintos (invéntalos).
Imprime el promedio, el máximo, el mínimo y la desviación estándar, redondeados a 2 decimales.
"""
consumo_gb = np.array([1.5, 2.3, 1.8, 2.0, 1.2, 2.5, 1.9])
promedio = np.round(np.mean(consumo_gb), 2)
maximo = np.round(np.max(consumo_gb), 2)
minimo = np.round(np.min(consumo_gb), 2)
desviacion_estandar = np.round(np.std(consumo_gb), 2)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Desviación estándar:", desviacion_estandar)


#ARRAYS DE DOS DIMENCIONES

"""
INSTRUCCIÓN:
Con esta matriz, donde cada fila es un estudiante y cada columna es una semana de horas de estudio,
calcula el promedio de horas de cada estudiante y el promedio de cada semana entre todos los estudiantes.
"""
horas_estudio = np.array([[5, 8, 6, 7],
                          [10, 9, 11, 8],
                          [3, 4, 2, 5]])
promedio_estudiantes = np.mean(horas_estudio, axis=1)
promedio_semanas = np.mean(horas_estudio, axis=0),
print("Promedio de horas de cada estudiante:", promedio_estudiantes)
print("Promedio de horas de cada semana entre todos los estudiantes:", promedio_semanas)


#VENTAS SEMANALES DE 3 SUCURSALES 

"""
PROBLEMA:
Calcula:
(1) el total de ventas de cada sucursal en la semana,
(2) una comisión del 5% sobre el total de cada sucursal,
(3) el total de ventas combinadas de las 3 sucursales por cada día de la semana.
"""
ventas = np.array([
    [1200, 1350, 980, 1420, 1100],
    [850, 920, 1050, 890, 960],
    [1600, 1750, 1580, 1690, 1720],
])
total_ventas_sucursales = np.sum(ventas, axis=1)
comisiones = total_ventas_sucursales * 0.05
total_ventas_semana = np.sum(ventas, axis=0)
print("Total de ventas de cada sucursal en la semana:", total_ventas_sucursales)
print("Comisión del 5% sobre el total de cada sucursal:", comisiones)
print("Total de ventas combinadas de las 3 sucursales por cada día de la semana:", total_ventas_semana)


#RETO ABIERTO

"""
INSTRUCCIÓN: 

Usando la misma matriz ventas del Desafío Final:
Determina cuál de las 3 sucursales tiene las ventas más consistentes a lo largo de la semana
(la que menos varía día a día, no la que más vende).
Imprime el resultado de las 3 sucursales para poder comparar.

Piensa en cuál de las 4 funciones estadísticas que ya usaste en el Paso 3 mide "variación",
no "total" ni "promedio".
"""
import numpy as np
ventas = np.array([
    [1200, 1350, 980, 1420, 1100],
    [850, 920, 1050, 890, 960],
    [1600, 1750, 1580, 1690, 1720],
])

variacion_sucursales = np.std(ventas, axis=1, ddof=0)
variacion_redondeada = np.round(variacion_sucursales, 2)
print("Sucursal 1: desviación estándar =", variacion_redondeada[0])
print("Sucursal 2: desviación estándar =", variacion_redondeada[1])
print("Sucursal 3: desviación estándar =", variacion_redondeada[2])