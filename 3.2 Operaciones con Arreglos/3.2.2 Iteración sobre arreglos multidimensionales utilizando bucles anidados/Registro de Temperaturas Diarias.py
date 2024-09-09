import random

# Definir las dimensiones de la matriz 3D
ciudades = ["CiudadA", "CiudadB", "CiudadC"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Generar la matriz 3D con temperaturas aleatorias entre 15 y 35 grados
matriz_temperaturas = [[[random.randint(15, 35) for _ in range(semanas)] for _ in range(len(dias_semana))] for _ in range(len(ciudades))]

# Calcular el promedio de temperaturas para cada ciudad por semana utilizando bucles anidados
for i in range(len(ciudades)):
    print(f"Promedio de temperaturas para {ciudades[i]}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += matriz_temperaturas[i][dia][semana]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
