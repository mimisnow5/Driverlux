import json

ARCHIVO_JSON = "drivers.json"

def guardar_datos(datos):
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def leer_datos():
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
