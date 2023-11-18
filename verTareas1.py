import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget, QTabWidget


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

        # QTabWidget para las pestañas
        self.tabs = QTabWidget(self)
        self.tabs.setGeometry(10, 70, self.ancho - 20, self.alto - 80)

        # Llama al método para cargar y mostrar las tareas en las pestañas
        self.cargar_tareas()

        # Botón para volver al menú principal
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(200)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(fuente2)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.volverMenu.move(325, 520)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cargar_tareas(self):
        tipos_trabajador = ["Chef", "Jardinero", "Enfermero"]

        for tipo in tipos_trabajador:
            try:
                with open(f"{tipo.lower()}_tareas.txt", "r") as file:
                    tareas = file.read()
                    self.agregar_tab(tipo, tareas)
            except FileNotFoundError:
                self.agregar_tab(tipo, "No hay tareas disponibles.")

    def agregar_tab(self, tipo, tareas):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        textoHistorial = QTextEdit(tab)
        textoHistorial.setReadOnly(True)
        textoHistorial.setPlainText(tareas)

        layout.addWidget(textoHistorial)

        self.tabs.addTab(tab, tipo)

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
