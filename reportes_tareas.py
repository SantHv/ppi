import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QVBoxLayout, QWidget

class reportes_tareas(QMainWindow):
    def __init__(self):
        super(reportes_tareas, self).__init__()

        self.setWindowTitle("Tareas")
        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))
        self.ancho = 800
        self.alto = 600
        self.resize(self.ancho, self.alto)

        # Centra la ventana
        pantalla = self.frameGeometry()
        centro = QApplication.desktop().screenGeometry().center()
        pantalla.moveCenter(centro)
        self.move(pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Llamamos al método para establecer la imagen de fondo
        self.set_background_image("imagenes/fnd2e.png")

        # Fuente para letreros y botones
        fuente = QFont()
        fuente.setFamily("Arial")
        fuente.setPointSize(18)

        fuente2 = QFont()
        fuente2.setFamily("Arial")
        fuente2.setPointSize(10)

        # Agregar un QTextEdit para mostrar los reportes
        self.texto_reportes = QTextEdit(self)
        self.texto_reportes.setGeometry(50, 50, 700, 500)
        self.texto_reportes.setFont(fuente2)

        # Cargar los reportes al QTextEdit
        self.cargar_reportes()

    def cargar_reportes(self):
        try:
            with open("reportes_tareas.txt", 'r') as reportes_file:
                # Leer las líneas de los reportes
                reportes = reportes_file.readlines()

                # Crear una lista con dos espacios en blanco entre cada dos líneas de reporte
                reportes_con_espacios = [linea.strip() + '\n\n' for linea in reportes]

                # Unir la lista en un solo texto
                reportes_texto = ''.join(reportes_con_espacios)

            self.texto_reportes.setPlainText(reportes_texto)
        except FileNotFoundError:
            self.texto_reportes.setPlainText("No hay reportes disponibles.")

    def set_background_image(self, image_path):
        # Load the background image
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)

        # Create a QLabel for the background image
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)

        # Set the background image to be in the back of all other widgets
        background_label.lower()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = reportes_tareas()
    v1.show()
    sys.exit(aplicacion1.exec_())
