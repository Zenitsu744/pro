def calcular_cobro(tiempo_minutos):
    tarifa_por_minuto = 139
    total_sin_iva = tiempo_minutos * tarifa_por_minuto
    iva = total_sin_iva * 0.16  # Suponiendo un IVA del 16%
    total_con_iva = total_sin_iva + iva
    total_redondeado = round(total_con_iva / 50) * 50  # Redondear al siguiente múltiplo de $50
    
    return total_redondeado

def main():
    while True:
        print("Menú de Inicio")
        print("1. Calcular tiempo de parqueo")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            tiempo_minutos = int(input("Ingresa el tiempo de parqueo del en minutos: "))
            if tiempo_minutos > 0:
                total_cobro = calcular_cobro(tiempo_minutos)
                print(f"Total a pagar: ${total_cobro:.2f}")
            else:
                print("El tiempo de parqueo debe ser mayor a 0.")
        elif opcion == '2':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Ingresa 1 o 2.")

if __name__ == "__main__":
    main()

