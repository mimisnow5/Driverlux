import subprocess


def detectar_hardware():
    try:
        #Ejecutamos el comando el comando y guardamos su salida como texto en una variable "resultado":
        resultado = subprocess.run(["lspci", "-k"], capture_output=True, text=True)

        #guardo la salida del comando con splitlines en una variable llamada lineas:

        lineas = resultado.stdout.splitlines()

        #lista vacia donde se guardaran los diccionarios:
        
        categorias = {"VGA": "gpu", "Network": "red", "Audio": "audio", "USB": "usb", "Multimedia": "multimedia"}

        dispositivos = {"gpu": [], "red": [], "audio": [], "usb": [], "multimedia": []}
        #diccionario vacio donde se guardará los dispositivos:

        dispositivo_actual = None
        
        #lista fija de drivers:
        tipos = ["VGA", "Network", "Audio", "USB", "Multimedia"]

        for linea in lineas:
            for tipo in tipos:
                if tipo in linea:
                    nombre = linea.split(":")[-1].strip()
                    dispositivo_actual = {"tipo": tipo, "nombre": nombre, "driver": "Sin driver"}
                    
                    categoria = categorias[tipo]

                    dispositivos[categoria].append(dispositivo_actual)
            if "Kernel driver in use:" in linea:
                if dispositivo_actual:
                    driver = linea.split(":")[-1].strip()
                    dispositivo_actual["driver"] = driver


        return dispositivos
    #aplicamos una excepción si ocurre un error:
    except Exception as e:
        print(f"Error detectando hardware: {e}")
        #lista vacia para evitar que el programa se rompa:
        return []

