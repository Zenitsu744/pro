
from ast import main


def man(cadena):
    for i in range(len(cadena)):
        print(cadena[i])

def main2(cadena):
    for i in cadena:
        print(i)

if __name__=="__main__":
 cadena="Hola mundo"
main(cadena)
