from ast import main


def obtener_festivos(mes):
    festivos = {
        "Enero": ["Año Nuevo"],
        "Febrero": ["Día de San Valentín"],
        "Marzo": ["Día de San José"],
        "Abril": ["Día de Pascua"],
        "Mayo": ["Día del Trabajo"],
        "Junio": [],
        "Julio": [],
        "Agosto": [],
        "Septiembre": [],
        "Octubre": ["Día de Halloween"],
        "Noviembre": ["Día de Acción de Gracias"],
        "Diciembre": ["Navidad"]
    }
    return festivos.get(mes, [])

def obtener_dias_mes(mes):
    dias_por_mes = {
        "Enero": 31,
        "Febrero": 28,  # Esto lo tomamos suponiendo que no sea una año biciesto 
        "Marzo": 31,
        "Abril": 30,
        "Mayo": 31,
        "Junio": 30,
        "Julio": 31,
        "Agosto": 31,
        "Septiembre": 30,
        "Octubre": 31,
        "Noviembre": 30,
        "Diciembre": 31
    }
    return dias_por_mes.get(mes, "Mes no válido")

mes_ingresado = input("Ingrese el nombre de un mes del año: ")

dias_del_mes = obtener_dias_mes(mes_ingresado)
festivos_del_mes = obtener_festivos(mes_ingresado)

if dias_del_mes != "Mes no válido":
    print(f"{mes_ingresado} tiene {dias_del_mes} días.")
    if festivos_del_mes:
        print("Festivos:")
        for festivo in festivos_del_mes:
            print(f"- {festivo}")
    else:
        print("No hay festivos registrados para este mes.")
else:
    print("Mes no válido.")

if __name__=="__main__":
 main()