def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def encontrar_min_max(matriz):
    minimo = matriz[0][0]
    maximo = matriz[0][0]
    pos_min = (0, 0)
    pos_max = (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < minimo:
                minimo = matriz[i][j]
                pos_min = (i, j)
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                pos_max = (i, j)

    return minimo, maximo, pos_min, pos_max

def ordenar_matriz_descendente(matriz):
    matriz_flatten = [num for fila in matriz for num in fila]
    matriz_flatten.sort(reverse=True)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = matriz_flatten.pop(0)

# Crear matriz 5x10 con números aleatorios entre 1 y 100
import random

matriz = [[random.randint(1, 100) for _ in range(10)] for _ in range(5)]

print("Matriz original:")
imprimir_matriz(matriz)

minimo, maximo, pos_min, pos_max = encontrar_min_max(matriz)
print("\nNúmero más bajo:", minimo, "en la posición:", pos_min)
print("Número más alto:", maximo, "en la posición:", pos_max)

ordenar_matriz_descendente(matriz)
print("\nMatriz ordenada de mayor a menor:")
imprimir_matriz(matriz)
