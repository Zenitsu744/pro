ef determinar_tipo_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No es un triángulo"

def main():
    while True:
        print("Menú de Inicio")
        print("1. Determinar si se puede formar un triángulo y su tipo")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            lado1 = float(input("Ingresa la longitud del primer lado: "))
            lado2 = float(input("Ingresa la longitud del segundo lado: "))
            lado3 = float(input("Ingresa la longitud del tercer lado: "))
            
            tipo_triangulo = determinar_tipo_triangulo(lado1, lado2, lado3)
            print(f"Resultado: {tipo_triangulo}")
        elif opcion == '2':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Ingresa 1 o 2.")

if __name__ == "__main__":
    main()