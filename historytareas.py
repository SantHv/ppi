import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit

class HistorialTareas(QMainWindow):
    def __init__(self):
        super(HistorialTareas, self).__init__()

        self.setWindowTitle("Historial de Tareas")
        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))

        self.ancho = 800
        self.alto = 600
        self.resize(self.ancho, self.alto)

        pantalla = self.frameGeometry()
        centro = QApplication.desktop().screenGeometry().center()
        pantalla.moveCenter(centro)
        self.move(pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        self.set_background_image("imagenes/fnd2e.png")

        fuente = QFont()
        fuente.setFamily("Arial")
        fuente.setPointSize(18)

        fuente2 = QFont()
        fuente2.setFamily("Arial")
        fuente2.setPointSize(10)

        letrero1 = QLabel(self)
        letrero1.setText("Historial de Tareas")
        letrero1.setFont(fuente)
        letrero1.setStyleSheet("color: black; padding: 30px;")
        letrero1.setFixedWidth(400)
        letrero1.move(250, 40)

        self.textoHistorial = QTextEdit(self)
        self.textoHistorial.setPlaceholderText("Aquí se mostrará el historial de tareas.")
        self.textoHistorial.setReadOnly(True)
        self.textoHistorial.setGeometry(100, 100, 600, 400)

        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(200)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(fuente2)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.volverMenu.move(310, 520)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

        # Llama al método para cargar y mostrar el historial
        self.cargar_historial()

    def cargar_historial(self):
        try:
            with open("tareas.txt", "r") as file:
                historial = file.read()
                self.textoHistorial.setPlainText(historial)
        except FileNotFoundError:
            self.textoHistorial.setPlainText("El historial de tareas está vacío.")

    def cerrar_ventana(self):
        self.close()

    def set_background_image(self, image_path):
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)
        background_label.lower()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = HistorialTareas()
    v1.show()
    sys.exit(aplicacion1.exec_())
