import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QMessageBox

class ReportarTarea(QMainWindow):
    def __init__(self):
        super(ReportarTarea, self).__init__()

        self.setWindowTitle("Reportar Tarea")

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
        letrero1.setText("Reportar Tarea")
        letrero1.setFont(fuente)
        letrero1.setStyleSheet("color: #09B4AC; padding: 30px;")
        letrero1.setFixedWidth(300)
        letrero1.move(300, 40)

        # Área de texto para ingresar el reporte
        self.reporteTarea = QTextEdit(self)
        self.reporteTarea.setPlaceholderText("Escribe aquí tu reporte de la tarea...")
        self.reporteTarea.setGeometry(100, 100, 600, 300)

        # Botón para enviar el reporte
        self.enviarReporte = QPushButton(self)
        self.enviarReporte.setText("Enviar Reporte")
        self.enviarReporte.setFixedWidth(200)
        self.enviarReporte.setFixedHeight(40)
        self.enviarReporte.setFont(fuente2)
        self.enviarReporte.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.enviarReporte.move(325, 450)
        self.enviarReporte.clicked.connect(self.enviar_reporte)

        # Botón para volver al menú principal
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(200)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(fuente2)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.volverMenu.move(325, 521)

        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
            self.close()

    def enviar_reporte(self):
        # Obtener el texto del reporte
        reporte = self.reporteTarea.toPlainText()

        if reporte:
            # Aquí puedes agregar la lógica para enviar el reporte a tu sistema
            # Por ahora, simplemente mostraremos un mensaje de éxito
            QMessageBox.information(self, "Reporte Enviado", "El reporte se ha enviado con éxito.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Por favor, escribe un reporte antes de enviarlo.")
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
    v1 = ReportarTarea()
    v1.show()
    sys.exit(aplicacion1.exec_())