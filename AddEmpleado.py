import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QDesktopWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QApplication,
    QPushButton,
    QMainWindow,
    QComboBox,
    QMessageBox,
)

class Addemple1(QMainWindow):
    def __init__(self):
        super(Addemple1, self).__init__()

        self.setWindowTitle("Agregar Empleado")
        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))

        # Poner el color de fondo a la ventana

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 500
        self.alto = 400

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
        self.set_background_image("imagenes/fnd2e.png")

        # Hacemos el tipo de letra
        self.letra1 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra1.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra1.setPointSize(10)

        # Hacemos el tipo de letra
        self.letra2 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra2.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra2.setPointSize(12)

        # Hacemos el letrero
        self.login = QLabel(self)
        # Le escribimos el texto
        self.login.setText("Nombre:")
        # Le asignamos el tipo de letra
        self.login.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y márgenes al letrero
        self.login.setStyleSheet("background-color: #White; color: #0000FF; padding: 40px;")
        self.login.setFixedWidth(200)

        self.login.move(50, 100)

        # Hacemos el campo para ingresar el primer número
        self.editLogin = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editLogin.setFixedWidth(300)
        self.editLogin.setStyleSheet("background-color:White")
        # Establecemos que solo se ingrese un número máximo de 20 dígitos
        self.editLogin.setMaxLength(20)
        self.editLogin.move(50, 150)

        # Hacemos el letrero
        self.login = QLabel(self)
        # Le escribimos el texto
        self.login.setText("Puesto:")
        # Le asignamos el tipo de letra
        self.login.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y márgenes al letrero
        self.login.setStyleSheet("background-color: #White; color: #0000FF; padding: 40px;")
        self.login.setFixedWidth(200)

        self.login.move(50, 200)

        # Combo box para seleccionar el tipo de empleado
        self.employee_type_combo = QComboBox(self)
        self.employee_type_combo.addItems(["Jardinero", "Chef", "Enfermero"])
        self.employee_type_combo.setFixedWidth(200)
        self.employee_type_combo.setStyleSheet("background-color:white; color black")
        self.employee_type_combo.move(50, 240)

        # Hacemos un botón para hacer los cálculos
        self.botonCalcular = QPushButton(self)
        self.botonCalcular.setText("Agregar Empleado")
        # Establecemos el ancho del botón
        self.botonCalcular.setFixedWidth(300)
        # Le ponemos color de fondo, color de texto y márgenes al botón
        self.botonCalcular.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        # Ponemos el botón de 5 hacia abajo
        self.botonCalcular.move(50, 280)
        self.botonCalcular.clicked.connect(self.guardar_empleado)

        # Botón para volver al menú principal
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(150)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(self.letra1)
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 10px;")
        self.volverMenu.move(50, 320)
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

    def guardar_empleado(self):
        # Obtener los datos del empleado
        nombre = self.editLogin.text()
        puesto = self.employee_type_combo.currentText()

        # Crear una cadena con la información del empleado
        empleado_info = f"Nombre: {nombre}\nPuesto: {puesto}\n"

        # Escribir la información del empleado en un archivo de texto
        with open("empleados.txt", "a") as file:
            file.write(empleado_info + "\n")


        QMessageBox.information(self, "Éxito", "Empleado guardado con éxito.")
        self.editLogin.clear()

if __name__ == "__main__":
    # Creamos una aplicación PyQt5
    aplicacion1 = QApplication(sys.argv)
    # Creamos una ventana
    v1 = Addemple1()
    # Indicamos que la ventana se deje observar
    v1.show()
    # Indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())
