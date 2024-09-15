def calcular_temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de cada ciudad durante un período de tiempo.
    Args:
        ciudades_temperaturas (dict): Un diccionario donde las claves son nombres de ciudades
                                      y los valores son listas de temperaturas semanales.
    Returns:
        dict: Un diccionario con las ciudades y sus temperaturas promedio.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas_semanales in ciudades_temperaturas.items():
        # Unir todas las temperaturas en una sola lista
        todas_temperaturas = []
        for semana in temperaturas_semanales:
            todas_temperaturas.extend(semana)

        # Calcular el promedio
        promedio = sum(todas_temperaturas) / len(todas_temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Datos de ejemplo: 3 ciudades durante 4 semanas
ciudades_temperaturas = {
    "Ciudad A": [
        [22, 23, 21, 20, 19, 18, 17],  # Semana 1
        [24, 25, 22, 23, 21, 20, 19],  # Semana 2
        [26, 27, 25, 24, 23, 22, 21],  # Semana 3
        [28, 29, 27, 26, 25, 24, 23]  # Semana 4
    ],
    "Ciudad B": [
        [30, 31, 29, 28, 27, 26, 25],
        [32, 33, 31, 30, 29, 28, 27],
        [34, 35, 33, 32, 31, 30, 29],
        [36, 37, 35, 34, 33, 32, 31]
    ],
    "Ciudad C": [
        [18, 19, 17, 16, 15, 14, 13],
        [20, 21, 19, 18, 17, 16, 15],
        [22, 23, 21, 20, 19, 18, 17],
        [24, 25, 23, 22, 21, 20, 19]
    ]
}

# Llamada a la función
temperaturas_promedio = calcular_temperatura_promedio(ciudades_temperaturas)

# Mostrar los resultados
print("Temperaturas promedio por ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
