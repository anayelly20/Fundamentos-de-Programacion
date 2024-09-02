# matriz bidimensional (3x3)
matriz = [
    [12, 23, 34],
    [45, 56, 67],
    [78, 89, 90]
]

# Definir la función de búsqueda
def buscar_en_matriz(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return f"Valor {valor_buscado} encontrado en la posición ({i}, {j})"
    return f"Valor {valor_buscado} no encontrado en la matriz"

# El valor a buscar
valor_buscado = 89

# Llamar la función y mostrar el resultado
resultado = buscar_en_matriz(matriz, valor_buscado)
print(matriz)
print(resultado)