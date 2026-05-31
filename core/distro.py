import platform

def info_distro():
    try:
        #Esto da un diccionario con toda la info de la distro
        data = platform.freedesktop_os_release()

        id_distro = data.get('ID')
        nombre = data.get('PRETTY_NAME')
        base = data.get('ID_LIKE', id_distro)
        
        kernel = platform.release()

        return id_distro, nombre, base, kernel
    except Exception:
        return ("desconocido", "Sistema no compatible", "desconocido", "desconocido")


