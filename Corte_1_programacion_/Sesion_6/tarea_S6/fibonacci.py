def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    
    return fib_series

def main():
    cantidad_digitos = int(input("Ingresa la cantidad de números de la serie de Fibonacci a mostrar: "))
    
    if cantidad_digitos <= 0:
        print("Por favor, ingresa una cantidad válida mayor a 0.")
    else:
        fib_series = fibonacci(cantidad_digitos)
        fib_series.sort()  # Ordenar la serie de menor a mayor para que se vea mejor 
        print(f"Los primeros {cantidad_digitos} números de la serie de Fibonacci en orden son:")
        for num in fib_series:
            print(num)

if __name__ == "__main__":
    main()