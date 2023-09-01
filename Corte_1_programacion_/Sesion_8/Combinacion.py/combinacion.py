from factorial import factorial as f 

def main():
    n=int(input("Ingrese el numero de elementos"))
    m=int(input("ingrese el numero de grupos "))
    cmb=(f(n)/(f(m)*(f(n-m))))
    print("el numero posible de convinaciones es cmb")


if __name__=="__main__":
    main()