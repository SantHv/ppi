import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton, \
    QMainWindow
from historytareas import HistorialTareas
from PyQt5 import QtGui
from reportTask import ReportarTarea
from verTareas1 import VerTareas


class Login3(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(Login3,self).__init__()

        self.setWindowTitle("Empleado")

        # Poner el color  de fondo a la ventana

        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 1000
        self.alto = 400

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Estas lineas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para que la ventana no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        self.set_background_image("imagenes/fnd2e.png")



        # Hacemos el tipo de letra
        self.letra1 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra1.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra1.setPointSize(18)

        # Hacemos el tipo de letra
        self.letra2 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra2.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra2.setPointSize(10)

        # Hacemos el letrero
        self.letrero1 = QLabel(self)
        # Le escribimos el texto
        self.letrero1.setText("Menu Empleado")
        # Le asignamos el tipo de letra
        self.letrero1.setFont(self.letra1)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.letrero1.setStyleSheet("color: black; padding: 30px;")
        self.letrero1.setFixedWidth(350)


        self.letrero1.move(380, 40)

        # Hacemos un boton para hacer los calculos
        self.vertareas = QPushButton(self)
        self.vertareas.setText("Ver Tareas")
        # Establecemos el ancho del boton
        self.vertareas.setFixedWidth(300)
        self.vertareas.setFixedHeight(40)
        self.vertareas.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.vertareas.setStyleSheet("background-color: #50D4FA; color: #000000; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.vertareas.move(190, 100)
        self.vertareas.clicked.connect(self.abrir_ventana_ver_tareas)

        # Hacemos un boton para hacer los calculos
        self.reportTask = QPushButton(self)
        self.reportTask.setText("Reportar Tarea")
        # Establecemos el ancho del boton
        self.reportTask.setFixedWidth(300)
        self.reportTask.setFixedHeight(40)
        self.reportTask.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.reportTask.setStyleSheet("background-color: #50D4FA; color: #000000; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.reportTask.move(560, 100)
        self.reportTask.clicked.connect(self.abrir_ventana_report_task)
        # Hacemos un boton para hacer los calculos
        self.historyTask = QPushButton(self)
        self.historyTask.setText("Historial de Tareas")
        # Establecemos el ancho del boton
        self.historyTask.setFixedWidth(300)
        self.historyTask.setFixedHeight(40)
        self.historyTask.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.historyTask.setStyleSheet("background-color: #50D4FA; color: #000000; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.historyTask.move(560, 200)
        self.historyTask.clicked.connect(self.abrir_ventana_history_task)
    def set_background_image(self, image_path):
        # Load the background image
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)

        # Create a QLabel for the background image
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)

        # Set the background image to be in the back of all other widgets
        background_label.lower()
    def abrir_ventana_history_task(self):
        self.ventana_history_task = HistorialTareas()
        self.ventana_history_task.show()

    def abrir_ventana_report_task(self):
        self.ventana_report_task = ReportarTarea()
        self.ventana_report_task.show()

    def abrir_ventana_ver_tareas(self):
        self.ventana_ver_tareas = VerTareas()
        self.ventana_ver_tareas.show()



# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = Login3()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())