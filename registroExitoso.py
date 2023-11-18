import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton, \
    QMainWindow, QMessageBox
from ventana2 import Login2
from ventana3 import Login3
from registrar import registrar1

class Login5(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(Login5,self).__init__()




        QMessageBox.information(self, 'Éxito', 'Inicio de sesión exitoso.')

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