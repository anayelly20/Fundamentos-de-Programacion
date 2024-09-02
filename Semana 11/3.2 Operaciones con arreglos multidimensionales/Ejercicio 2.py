# Matriz 3x3
matriz = [
    [40, 60, 10],
    [10, 80, 50],
    [90, 50, 70]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
                print("Estado intermedia de la fila:", fila)

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar
fila_a_ordenar = 1

# Ordenar la fila específica
bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila", fila_a_ordenar + 1, "ordenada:")
for fila in matriz:
    print(fila)
