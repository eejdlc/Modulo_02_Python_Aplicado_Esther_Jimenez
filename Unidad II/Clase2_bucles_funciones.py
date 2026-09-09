# Bucle for
edades = [24, 31, 19, 45, 27]

suma = 0
for edad in edades:
    suma += edad

print("suma total:", suma)
print("Promedio:", suma / len(edades))

"""
ejercicio - con la misma lista que utilizamos "edades" contar cuantas edades son mayores o iguales a 30, utilizar el bucle "for" y una variable contadora.
variable contadora: es una variable que empieza en 0 y le suma 1 cada vez que se cumple la condicion. ejemplo: contador += 1

pista: necesitar combinar lo que vimos ahora con el bucle for con lo que ustedes aprendiendo en la clase pasada "condicionales"
"""
Contador = 0
for edad in edades:
    if edad >= 30:
        Contador += 1 
print("Cantidad de edades mayores o iguales a 30:", Contador)

# Bucle While
contador = 1
while contador <= 5:
    print("vuelta - numero", contador)
    contador += 1

"""
ejercicio - while: utilicen "while", hagan una cuenta regresiva desde 5 hasta 1 y al final impriman "Iniciamos"
"""
Numero = 5
while Numero >= 1:
    print(Numero)
    Numero -= 1
print("Iniciamos")

# Funciones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

resultado = calcular_imc(70, 1.75)
print(f"IMC:{round(resultado, 2)}")

"""
Escribir una funcion le llamaran "clasificar_imc(imc) que reciba un IMC y devuelva un texto: "bajo de peso" si es menor a 18.5. "peso normal" si esta entre 18.5 y 25
"sobrepeso" si esta entre 25 y 30, "obesidad" si es de 30 o mas. despues, llamar el "resultado" de la funcion anterior.
"""
def clasificar_imc(imc):
    if imc < 18.5:
        return "bajo de peso"
    elif 18.5 <= imc < 25:
        return "peso normal"
    elif 25 <= imc < 30:
        return "sobrepeso"
    else:
        return "obesidad"

print(clasificar_imc(resultado))