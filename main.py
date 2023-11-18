import os
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton, \
    QMainWindow, QMessageBox, QCheckBox, QComboBox
from ventana2 import Login2
from ventana3 import Login3
from registrar import registrar1

class Login5(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(Login5,self).__init__()


        self.setWindowTitle("Inicio de sesion")
        self.setWindowIcon(QtGui.QIcon("imagenes/icono1.png"))





        # Estableciendo las propiedades de ancho y alto
        self.ancho = 900
        self.alto = 600


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

        # Set the background image
        self.set_background_image("imagenes/fnd1.png")
        # Hacemos el tipo de letra
        self.letra1 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra1.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra1.setPointSize(18)

        self.logo_label = QLabel(self)
        pixmap = QPixmap("imagenes/DOM1.png")
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setFixedSize(pixmap.size())  # Use the size of the pixmap
        self.logo_label.move(485, 220)  # Adjust the position as needed

        # Hacemos el tipo de letra
        self.letra2 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra2.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra2.setPointSize(16)

        # Hacemos el letrero
        self.letrero1 = QLabel(self)
        # Le escribimos el texto
        self.letrero1.setText("Domestic Space")
        # Le asignamos el tipo de letra
        self.letrero1.setFont(self.letra1)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.letrero1.setStyleSheet("background-color:color: #09B4AC; padding: 50px;")
        self.letrero1.setFixedWidth(500)

        self.letrero1.move(340, 30)

        # Hacemos el letrero
        self.login = QLabel(self)
        # Le escribimos el texto
        self.login.setText("Usuario")
        # Le asignamos el tipo de letra
        self.login.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.login.setStyleSheet("background-color: #White; color: #0000FF; padding: 40px;")
        self.login.setFixedWidth(250)
        self.login.move(305,100)






        # Hacemos el campo para ingresar el primer numero
        self.editLogin = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editLogin.setFixedWidth(250)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editLogin.setMaxLength(20)
        self.editLogin.setStyleSheet("background-color: white")

        self.editLogin.move(305, 160)

        # Hacemos el letrero
        self.contraseña = QLabel(self)
        # Le escribimos el texto
        self.contraseña.setText("Contraseña")
        # Le asignamos el tipo de letra
        self.contraseña.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.contraseña.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.contraseña.setFixedWidth(200)

        self.contraseña.move(305, 200)

        # Hacemos el campo para ingresar el primer numero
        self.editContraseña = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editContraseña.setFixedWidth(250)
        self.editContraseña.setStyleSheet("background-color: white")
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editContraseña.setMaxLength(20)
        self.editContraseña.setEchoMode(QLineEdit.Password)
        self.editContraseña.move(305, 240)

        self.tipoUsuario = QLabel(self)
        self.tipoUsuario.setText("Tipo de Usuario")
        self.tipoUsuario.setFont(self.letra2)
        self.tipoUsuario.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.tipoUsuario.setFixedWidth(200)
        self.tipoUsuario.move(305, 280)

        # Combo box para seleccionar el tipo de usuario
        self.user_type_combo = QComboBox(self)
        self.user_type_combo.addItems(["Empleado", "Empleador"])
        self.user_type_combo.setStyleSheet("background-color: White; color: black")
        self.user_type_combo.setFixedWidth(250)
        self.user_type_combo.move(305, 320)

        self.botonCalcular = QPushButton(self)
        self.botonCalcular.setText("Iniciar Sesión")
        self.botonCalcular.setFixedWidth(200)
        self.botonCalcular.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.botonCalcular.move(325, 450)
        self.botonCalcular.setFixedHeight(40)

        self.botonRegistrar = QPushButton(self)
        self.botonRegistrar.setText("Registrarse")
        self.botonRegistrar.setFixedWidth(200)
        self.botonRegistrar.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.botonRegistrar.move(325, 500)
        self.botonRegistrar.setFixedHeight(40)

        # Create a checkbox for toggling password visibility
        self.mostrar_contraseña_checkbox = QCheckBox("Mostrar Contraseña", self)
        self.mostrar_contraseña_checkbox.move(570, 240)
        self.mostrar_contraseña_checkbox.setFixedWidth(200)
        self.mostrar_contraseña_checkbox.stateChanged.connect(self.toggle_password_visibility)


        # Conectamos el botón a la función que verifica las credenciales
        self.botonCalcular.clicked.connect(self.check_login)

        # Conectamos el botón a la función que verifica las credenciales
        self.botonRegistrar.clicked.connect(self.abrir_registrar)
    def abrir_registrar(self):
        self.boton_Registrar = registrar1()
        self.boton_Registrar.show()

    def set_background_image(self, image_path):
        # Load the background image
        background_image = QPixmap(image_path).scaled(self.ancho, self.alto)

        # Create a QLabel for the background image
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, self.ancho, self.alto)

        # Set the background image to be in the back of all other widgets
        background_label.lower()

    def check_login(self):
        # Obtenemos el nombre de usuario y contraseña ingresados
        username = self.editLogin.text()
        password = self.editContraseña.text()
        tipo_usuario = self.user_type_combo.currentText()  # Corrige esto para obtener el valor correcto
        # Obtenemos la ruta del directorio del script actual
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Combinamos la ruta del directorio con el nombre del archivo
        registros_file = os.path.join(script_dir, 'registros.txt')
        # Intentamos abrir el archivo "registros.txt" en modo lectura
        try:
            with open('registros.txt', 'r') as archivo:
                # Leemos el contenido del archivo línea por línea
                lineas = archivo.readlines()

            # Creamos una lista de diccionarios para almacenar los datos de usuarios
            usuarios = []
            usuario_actual = {}
            for linea in lineas:
                linea = linea.strip()  # Eliminamos espacios en blanco y saltos de línea
                if linea:
                    clave, valor = linea.split(': ')
                    usuario_actual[clave] = valor
                else:
                    usuarios.append(usuario_actual)
                    usuario_actual = {}

            # Buscamos si las credenciales coinciden con algún usuario
            for usuario in usuarios:
                if (
                        usuario.get("Usuario") == username and
                        usuario.get("Contraseña") == password and
                        usuario.get("TipoUsuario") == tipo_usuario  # Comparamos el tipo de usuario

                ):

                    QMessageBox.information(self, 'Éxito', 'Inicio de sesión exitoso.')

                    if tipo_usuario == "Empleador":
                        self.abrir_ventana2()
                    elif tipo_usuario == "Empleado":
                        self.abrir_ventana33()
                    break

            else:
                QMessageBox.warning(self, 'Error', 'Credenciales incorrectas.')
        except FileNotFoundError:
            QMessageBox.warning(self, 'Error', 'No se encontró el archivo "registros.txt".')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Error al leer el archivo: {str(e)}')

    def abrir_ventana2(self):
            self.ventana2 = Login2()
            self.ventana2.show()
            self.hide()

    def abrir_ventana33(self):
            self.ventana33 = Login3()
            self.ventana33.show()
            self.hide()
    def toggle_password_visibility(self, state):
        if state == Qt.Checked:
            self.editContraseña.setEchoMode(QLineEdit.Normal)
        else:
            self.editContraseña.setEchoMode(QLineEdit.Password)









# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = Login5()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())