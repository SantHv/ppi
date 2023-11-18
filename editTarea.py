import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton, \
    QMainWindow


class editTarea1(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(editTarea1,self).__init__()

        self.setWindowTitle("EDITAR TAREA")

        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))

        # Poner el color  de fondo a la ventana


        # Estableciendo las propiedades de ancho y alto
        self.ancho = 500
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
        self.login.setText("ID de la Tarea:")
        # Le asignamos el tipo de letra
        self.login.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.login.setStyleSheet("background-color: #White; color: #0000FF; padding: 40px;")
        self.login.setFixedWidth(200)

        self.login.move(50, 100)

        # Hacemos el campo para ingresar el primer numero
        self.editLogin = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editLogin.setFixedWidth(300)
        self.editLogin.setStyleSheet("background-color: White")
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editLogin.setMaxLength(20)

        self.editLogin.move(50, 150)

        # Hacemos un boton para hacer los calculos
        self.editTarea = QPushButton(self)
        self.editTarea.setText("Editar Tarea")
        # Establecemos el ancho del boton
        self.editTarea.setFixedWidth(300)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.editTarea.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.editTarea.move(50,200)



        # Hacemos un boton para hacer los calculos
        self.eliminarTarea = QPushButton(self)
        self.eliminarTarea.setText("Eliminar Tarea")
        # Establecemos el ancho del boton
        self.eliminarTarea.setFixedWidth(300)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.eliminarTarea.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.eliminarTarea.move(50, 240)

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





# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = editTarea1()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())