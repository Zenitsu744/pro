from ast import main
import math

def calcular_modulo_vector(x1, y1, x2, y2):
    # Primero se debe calcular la diferencia entre las cordenadas 
    dx = x2 - x1
    dy = y2 - y1
    
    # Ahora calculamos el modulo del vector 
    modulo = math.sqrt(dx*2 + dy*2)
    
    return modulo, dx, dy

# Se solicita las cordenadas al usuario 
x1 = float(input("Ingrese la coordenada x del punto de origen: "))
y1 = float(input("Ingrese la coordenada y del punto de origen: "))
x2 = float(input("Ingrese la coordenada x del punto final: "))
y2 = float(input("Ingrese la coordenada y del punto final: "))

# Se calcula los modulos rectangulares del vector 
modulo, dx, dy = calcular_modulo_vector(x1, y1, x2, y2)

# Para finalizar se imprimen los rsultados sados anteriormente por el usuario 
print("El módulo del vector es:", modulo)

print("Las componentes rectangulares del vector son:")

print("Componente en x:", dx)

print("Componente en y:", dy)
if __name__=="__main__":
 main()
