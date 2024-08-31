# matriz de 3x3
matriz = [[3, 6, 9], [12, 15, 18], [21, 24, 27]]

print(matriz)

# función buscar_valor específico
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):  # Cambiado len(matriz) por len(matriz[i])
            if matriz[i][j] == valor_buscado:
                return i, j

#buscar la posicion de la matriz
valor_buscado = 6
print(buscar_valor(matriz, valor_buscado))

#si el valor fue encontrado imprime comentario
if valor_buscado == valor_buscado:
    print ("Valor encontrado en la posicion")

#Si el valor no fue encontrado imprime comentario
else:
    print ("Valor no encontrado")