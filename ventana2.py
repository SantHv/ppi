import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Importa tus otras clases
from addTarea import addtarea11
from AddEmpleado import Addemple1
from editTarea import editTarea1
from historytareas import HistorialTareas

class Login2(QMainWindow):
    def __init__(self):
        super(Login2, self).__init__()

        self.setWindowTitle("Empleador")

        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))
        self.ancho = 1200
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
        letrero1.setText("Menu Empleador")
        letrero1.setFont(fuente)
        letrero1.setStyleSheet("color: Black; padding: 30px;")
        letrero1.setFixedWidth(300)
        letrero1.move(450, 40)

        # Botón para agregar tarea
        self.addTarea = QPushButton(self)
        self.addTarea.setText("Agregar Tarea y Especificacion")
        self.addTarea.setFixedWidth(350)
        self.addTarea.setFixedHeight(40)
        self.addTarea.setFont(fuente2)
        self.addTarea.setStyleSheet("background-color: #50D4FA; color: #000000; padding: 30px;")
        self.addTarea.move(220, 280)
        self.addTarea.clicked.connect(self.abrir_ventana_add_tarea)

        # Botón para historial de tareas
        self.historyTask = QPushButton(self)
        self.historyTask.setText("Historial de Tareas")
        self.historyTask.setFixedWidth(350)
        self.historyTask.setFixedHeight(40)
        self.historyTask.setFont(fuente2)
        self.historyTask.setStyleSheet("background-color: #50D4FA; color: #000000; padding: 30px;")
        self.historyTask.move(600, 280)
        self.historyTask.clicked.connect(self.abrir_ventana_history_task)

        # Botón para editar tarea o eliminar
        self.ediTareaclean = QPushButton(self)
        self.ediTareaclean.setText("Editar Tarea o Eliminar")
        self.ediTareaclean.setFixedWidth(350)
        self.ediTareaclean.setFixedHeight(40)
        self.ediTareaclean.setFont(fuente2)
        self.ediTareaclean.setStyleSheet("background-color: #50D4FA; color: #000000; padding: 30px;")
        self.ediTareaclean.move(600, 200)
        self.ediTareaclean.clicked.connect(self.abrir_ventana_edit_tarea)

        # Botón para agregar empleado
        self.addEmpleado = QPushButton(self)
        self.addEmpleado.setText("Agregar Emplead@")
        self.addEmpleado.setFixedWidth(350)
        self.addEmpleado.setFixedHeight(40)
        self.addEmpleado.setFont(fuente2)
        self.addEmpleado.setStyleSheet("background-color: #50D4FA; color: #000000; padding: 30px;")
        self.addEmpleado.move(220, 200)
        self.addEmpleado.clicked.connect(self.abrir_ventana_add_empleado)
    def set_background_image(self, image_path):
        # Load the background image
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)

        # Create a QLabel for the background image
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)

        # Set the background image to be in the back of all other widgets
        background_label.lower()

    def abrir_ventana_add_tarea(self):
        self.ventana_add_tarea = addtarea11()
        self.ventana_add_tarea.show()

    def abrir_ventana_add_empleado(self):
        self.ventana_add_empleado = Addemple1()
        self.ventana_add_empleado.show()
    
    def abrir_ventana_edit_tarea(self):
        self.ventana_edit_tarea = editTarea1()
        self.ventana_edit_tarea.show()

    def abrir_ventana_history_task(self):
        self.ventana_history_task = HistorialTareas()
        self.ventana_history_task.show()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = Login2()
    v1.show()
    sys.exit(aplicacion1.exec_())