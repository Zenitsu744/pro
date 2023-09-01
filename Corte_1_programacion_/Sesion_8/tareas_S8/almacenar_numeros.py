def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

numeros = []
numero = int(input("Ingrese un número (ingrese un número negativo para terminar): "))

while numero >= 0:
    numeros.append(numero)
    numero = int(input("Ingrese otro número (ingrese un número negativo para terminar): "))

print("Lista original:")
print(numeros)

numeros_sin_duplicados = eliminar_duplicados(numeros)

print("Lista sin duplicados:")
print(numeros_sin_duplicados)
