import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit

class VerTareas(QMainWindow):
    def __init__(self):
        super(VerTareas, self).__init__()

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

        # Letrero
        letrero1 = QLabel(self)
        letrero1.setText("Ver Tareas")
        letrero1.setFont(fuente)
        letrero1.setStyleSheet("color: black; padding: 30px;")
        letrero1.setFixedWidth(400)
        letrero1.move(300, 40)

        # Área de texto para mostrar las tareas
        self.textoHistorial = QTextEdit(self)
        self.textoHistorial.setReadOnly(True)
        self.textoHistorial.setGeometry(100, 100, 600, 400)

        # Botón para volver al menú principal
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(200)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(fuente2)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.volverMenu.move(325, 520)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

        # Llama al método para cargar y mostrar las tareas
        self.cargar_tareas()

    def cargar_tareas(self):
        try:
            with open("tareas.txt", "r") as file:
                tareas = file.read()
                self.textoHistorial.setPlainText(tareas)
        except FileNotFoundError:
            self.textoHistorial.setPlainText("No hay tareas disponibles.")

    def set_background_image(self, image_path):
        # Load the background image
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)

        # Create a QLabel for the background image
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)

        # Set the background image to be in the back of all other widgets
        background_label.lower()

    def cerrar_ventana(self):
        self.close()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = VerTareas()
    v1.show()
    sys.exit(aplicacion1.exec_())
