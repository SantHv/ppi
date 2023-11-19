import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QWidget,
    QDesktopWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QApplication,
    QPushButton,
    QMainWindow,
    QMessageBox,
    QComboBox,
    QCalendarWidget,
)

class addtarea11(QMainWindow):
    def __init__(self):
        super(addtarea11, self).__init__()

        self.setWindowTitle("Agregar Tarea")
        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 800
        self.alto = 600

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Estas líneas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para que la ventana no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Llamamos al método para establecer la imagen de fondo
        self.set_background_image("imagenes/fnd2e.png")

        # Hacemos el tipo de letra
        self.letra1 = QFont()
        self.letra1.setFamily("Arial")
        self.letra1.setPointSize(12)

        # Hacemos el tipo de letra
        self.letra2 = QFont()
        self.letra2.setFamily("Arial")
        self.letra2.setPointSize(12)

        # Variable para mantener un contador de IDs
        self.id_counter = 1

        # Hacemos el letrero
        self.letrero1 = QLabel(self)
        self.letrero1.setText("Tipo de Trabajador:")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setStyleSheet("color: black; padding: 30px;")
        self.letrero1.setFixedWidth(250)
        self.letrero1.move(0, 20)

        # Lista desplegable para elegir el tipo de trabajador
        self.tipoTrabajadorCombo = QComboBox(self)
        self.tipoTrabajadorCombo.addItems(["Chef", "Enfermero", "Jardinero"])
        self.tipoTrabajadorCombo.setFixedWidth(400)
        self.tipoTrabajadorCombo.move(30, 45)

        # Hacemos el letrero
        self.letrero2 = QLabel(self)
        self.letrero2.setText("Titulo De la Tarea:")
        self.letrero2.setFont(self.letra1)
        self.letrero2.setStyleSheet("color: black; padding: 30px;")
        self.letrero2.setFixedWidth(250)
        self.letrero2.move(0, 80)

        # Hacemos el campo para ingresar el título de la tarea
        self.titleTask = QLineEdit(self)
        self.titleTask.setFixedWidth(400)
        self.titleTask.setStyleSheet("background-color: White")
        self.titleTask.setMaxLength(100)
        self.titleTask.move(30, 105)

        # Hacemos el letrero
        self.Qlabel1 = QLabel(self)
        self.Qlabel1.setText("Especificaciones:")
        self.Qlabel1.setFont(self.letra2)
        self.Qlabel1.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.Qlabel1.setFixedWidth(200)
        self.Qlabel1.move(30, 140)
        # Establecer la alineación vertical en la parte superior

        # Hacemos el campo para ingresar las especificaciones de la tarea
        self.Qline1 = QLineEdit(self)
        self.Qline1.setFixedWidth(400)
        self.Qline1.setStyleSheet("background-color: White")
        self.Qline1.setMaxLength(300)
        self.Qline1.setFixedHeight(200)
        self.Qline1.move(30, 170)
        # Establecer la alineación vertical en la parte superior
        self.Qline1.setAlignment(Qt.AlignTop)
        # Establecer la alineación vertical en la parte superior
        self.Qline1.setAlignment(Qt.AlignTop)

        # Hacemos el letrero
        self.letrero3 = QLabel(self)
        self.letrero3.setText("Fecha de Tarea:")
        self.letrero3.setFont(self.letra1)
        self.letrero3.setStyleSheet("color: black; padding: 30px;")
        self.letrero3.setFixedWidth(250)
        self.letrero3.move(420, 100)

        # Agregar el calendario
        self.calendarWidget = QCalendarWidget(self)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setGeometry(450, 170, 300, 310)

        # Hacemos un botón para agregar la tarea
        self.botonTarea = QPushButton(self)
        self.botonTarea.setText("Agregar Tarea")
        self.botonTarea.setFixedWidth(400)
        self.botonTarea.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.botonTarea.move(30, 400)
        self.botonTarea.clicked.connect(self.guardar_tarea)

        # Hacemos un botón para volver al menú
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver Menu")
        self.volverMenu.setFixedWidth(400)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.volverMenu.move(30, 450)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
        self.close()

    def set_background_image(self, image_path):
        # Load the background image
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)

        # Create a QLabel for the background image
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)

        # Set the background image to be in the back of all other widgets
        background_label.lower()

    def guardar_tarea(self):
        # Obtener los datos de la tarea
        tipo_trabajador = self.tipoTrabajadorCombo.currentText()
        titulo_tarea = self.titleTask.text()
        especificaciones_tarea = self.Qline1.text()
        fecha_tarea = self.calendarWidget.selectedDate().toString(Qt.ISODate)

        # Añadir un ID único a la tarea
        tarea_info = f"ID: {self.id_counter}\nTipo de Trabajador: {tipo_trabajador}\nTítulo: {titulo_tarea}\nEspecificaciones: {especificaciones_tarea}\nFecha: {fecha_tarea}\n"

        # Incrementar el contador de IDs
        self.id_counter += 1

        # Crear una cadena con la información de la tarea
        tarea_info = f"Tipo de Trabajador: {tipo_trabajador}\nTítulo: {titulo_tarea}\nEspecificaciones: {especificaciones_tarea}\nFecha: {fecha_tarea}\n"

        # Escribir la información de la tarea en un archivo de texto específico
        with open(f"{tipo_trabajador.lower()}_tareas.txt", "a") as file:
            file.write(tarea_info + "\n")

        QMessageBox.information(self, "Éxito", "Tarea agregada con éxito.")
        self.tipoTrabajadorCombo.setCurrentIndex(0)
        self.titleTask.clear()
        self.Qline1.clear()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = addtarea11()
    v1.show()
    sys.exit(aplicacion1.exec_())
