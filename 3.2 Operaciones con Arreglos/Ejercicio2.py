# Definimos una matriz 3x3 con valores enteros.
matriz = [[4, 2, 6], [12, 8, 10], [18, 16, 14]]

# Imprimimos la matriz original.
print(matriz)

# Definimos una función llamada 'buble_sort' que ordena una fila de la matriz usando el metodo de ordenamiento burbuja
def buble_sorft(fila):
    n = len(fila)  # Obtenemos la longitud de la fila.
    # Iteramos sobre la fila.
    for i in range(n):
        # En cada iteración, comparamos los elementos adyacentes en la fila.
        for j in range(n-1, i, -1):
            # Si el elemento actual es mayor que el anterior, los intercambiamos.
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                # Imprimimos la fila en cada paso para ver cómo se está ordenando.
                print(fila)

# Imprimimos la matriz original (antes de ordenar).
print("matriz original")
print(matriz)

# Aplicamos el metodo de ordenamiento burbuja a la segunda fila de la matriz (índice 1).
buble_sorft(matriz[1])

# Imprimimos la matriz después de ordenar la segunda fila.
print(matriz)
