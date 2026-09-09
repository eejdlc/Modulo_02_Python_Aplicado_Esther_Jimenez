# Ejercicio:
# Calcular cuántas vueltas completas se pueden correr con una distancia dada
# y cuántos metros sobran después de esas vueltas completas.

distancia_metros = 1500
vueltas_metros = 400

vueltas_completas = distancia_metros // vueltas_metros
metros_sobrantes = distancia_metros % vueltas_metros

print(f"Vueltas completas: {vueltas_completas}")
print(f"Metros sobrantes: {metros_sobrantes}")