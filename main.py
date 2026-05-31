import sys

from core import distro
from core import hardware

from core.jsondb import guardar_datos, leer_datos 

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class Drivelux(QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("drivelux.ui", self)
        
        # Fuerza que inicie en la página 0 del stackedWidget
        self.stackedWidget.setCurrentIndex(0)
        
        # Ejecuta la carga de datos
        self.mostrar_info()

    def mostrar_info(self):
        # 1. Carga info de distro.py
        try:
            id_s, name, like, kernel = distro.info_distro()
            self.lbl_distro.setText(f"{name}")
            self.lbl_kernel.setText(f"{kernel}")
        except Exception as e:
            print(f"Error cargando distro: {e}")

        # 2. Carga info de hardware y drivers
        try:
            dispositivos = hardware.detectar_hardware()
            guardar_datos(dispositivos)
            datos = leer_datos()
            self.lista_drivers.clear()
            for dispositivo in datos:
                #creamos una cadena legible
                info_texto = (
                    f"{dispositivo['tipo']} | "
                    f"{dispositivo['nombre']} | "
                    f"{dispositivo.get('driver', 'Sin driver')}"
                )
                self.lista_drivers.addItem(info_texto)
        except Exception as e:
            print(f"Error cargando hardware: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Drivelux()
    window.show()
    sys.exit(app.exec())
