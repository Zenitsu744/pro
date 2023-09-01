def es_vocal(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    return letra.lower() in vocales

def es_consonante(letra):
    return letra.isalpha() and not es_vocal(letra)

def main():
    while True:
        print("Menú de Inicio")
        print("1. Verificar si una letra es vocal o consonante")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            letra = input("Ingresa una letra del abecedario: ")
            if len(letra) == 1 and letra.isalpha():
                if es_vocal(letra):
                    print(f"{letra} es una vocal.")
                elif es_consonante(letra):
                    print(f"{letra} es una consonante.")
                else:
                    print("El carácter ingresado no es una letra.")
            else:
                print("Ingresa una única letra válida.")
        elif opcion == '2':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Ingresa 1 o 2.")

if __name__ == "__main__":
    main()