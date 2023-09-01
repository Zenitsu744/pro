def producto_por_sumas(numero1, numero2):
    if numero2 == 0:
        return 0
    elif numero2 > 0:
        return numero1 + producto_por_sumas(numero1, numero2 - 1)
    else:
        return -producto_por_sumas(numero1, -numero2)

def main():
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    
    resultado = producto_por_sumas(numero1, numero2)
    print(f"El producto de {numero1} y {numero2} es: {resultado}")

if __name__ == "__main__":
    main()