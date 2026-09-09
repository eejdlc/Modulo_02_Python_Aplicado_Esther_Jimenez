import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
print(df.shape)
print(list(df.columns))
print(df.head(3))

#Visualizar las primeras 5 filas del DataFrame
print(df.head(5))

#Imprimir solo la columna "Name" utilizando .head(3)
print(df["Name"].head(3))

subset_df = df[["Name", "Age", "Survived"]]
print(subset_df.head(3))

#Filtrar con una condición
mayores_30 = df[df["Age"] > 30]
print(mayores_30.shape)

mujeres = df[df["Sex"] == "female"]
print(mujeres.shape)

#combinar condiciones y contar valores
mujeres_sobrevivientes = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(mujeres_sobrevivientes.shape)
print(df["Survived"].value_counts())




# ejemplo de concepto "Series"
precios = pd.Series([25.99, 40.50, 15.75, 60.00])
print(precios)
print(type(precios))

# ejemplo de concepto "DataFrame"
productos = pd.DataFrame({
    "nombre": ["Audífonos", "Mouse", "Teclado"],
    "precio": [45.99, 15.50, 40.00],
    "stock": [120, 80, 45]
})

print(productos)

"""
EJERCICIO GUIADO

1. crear un DataFrame llamado estudiantes.
2. incluir 3 columnas con la llave: nombre, edad y curso. (con datos de 4 personas, inventarlo)
3. imprimir dataframe para visualizarlo

"""
Estudiantes = pd.DataFrame({
    "nombre": ["Ana", "Carlos", "Elena", "Luis"],
    "edad": [20, 22, 21, 23],
    "curso": ["Matemáticas", "Física", "Química", "Biología"]
})
print(Estudiantes)

#Eliminar valores de filas vacías
edades = df["Age"].dropna()

#Crear array de numpy con una Serie (pandas)
edades_array = edades.to_numpy()

print(type(edades_array))

#Fórmulas utilizadas en numpy para calcular
print("Promedio de edad:", round(np.mean(edades_array),1))
print("Edad maxima:", np.max(edades_array))
print("Edad minima:", np.min(edades_array))
print("Desviacion estandar:", round(np.std(edades_array),1))

"""
EJERCICIO GUIADO

1. filtrar el DataFrame para quedarse solo con los pasajeros de la columna "Pclass".
2. guardar en una variable nueva e imprimira cuantas filas tienes.
3. despues utilizar el metodo .value_counts() sobre la columna "Pclass" del DataFrame original.

objetivo: visualizar cuantos pasajeros habia en cada clase

"""
pasajeros_primera_clase = df[df["Pclass"] == 1]
print(pasajeros_primera_clase.shape)
print(df["Pclass"].value_counts())

