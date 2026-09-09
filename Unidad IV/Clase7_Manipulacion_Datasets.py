import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
print(df.shape)
#Eliminamos columna "cabin" porque tiene alrededor de un 77% de casos nulos
df = df.drop(columns=["Cabin"])

#Calcular la media de la columna "Age"
edad_mediana = df["Age"].median()
df["Age"] = df["Age"].fillna(edad_mediana)

#Eliminar filas vacías dentro de la columna "Embarked"
df = df.dropna(subset=["Embarked"])
print(df.shape)
print(df.isnull().sum().sum())

"""
EJERCICIO GUIADO: 
1. imprimir la cantidad de columnas que tenemos.
2. confirmar que la columna "Age" ya no tienes nulos
"""
print(list(df.columns))
print(df["Age"].isnull().sum())

#Crear columnas nuevas a través "feature engineering"
df["FamiliaTotal"] = df["SibSp"] + df["Parch"] + 1
print(df[["SibSp", "Parch", "FamiliaTotal"]].head())

#Crear columna para evaluar valores booleanos (True/False)
df["EsMenorDeEdad"] = df["Age"] < 18
print(df["EsMenorDeEdad"].value_counts())

#Identificar tipos de datos y ordenarlos
print(df.dtypes)

#Cambiar tipo de datos de una columna
df['Survived'] = df['Survived'].astype(bool)
print(df['Survived'].dtype)
print(df['Survived'].head(3))

#Ordenar el dataset
df_por_edad = df.sort_values("Age", ascending=False)
print(df_por_edad[["Name", "Age"]].head(3))

#Agrupar el dataset
promedio_edad_por_clase = df.groupby("Pclass")["Age"].mean()
print(promedio_edad_por_clase)

promedio_edad_por_clase = df.groupby("Pclass")["Survived"].mean()
print(promedio_edad_por_clase.round(3))

df.to_csv("titanic_limpio.csv", index=False)