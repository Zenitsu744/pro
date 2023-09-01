import random

# Generar 15 números aleatorios y almacenarlos en una lista
numeros_aleatorios = [random.randint(1, 100) for _ in range(15)]

print("Números aleatorios generados:")
print(numeros_aleatorios)

# Ordenar la lista de menor a mayor
numeros_aleatorios.sort()

print("Números ordenados de menor a mayor:")
print(numeros_aleatorios)
